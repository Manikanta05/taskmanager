from flask import Flask,render_template, url_for,request
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']=""
app.config['MYSQL_DB']="task_management"

mysql = MySQL(app)

@app.route('/')
def homePage():
    return render_template('index.html')

@app.route('/loginPage')
def loginPage():
    return render_template('login.html')

@app.route('/contactPage')
def contactPage():
    return render_template('contact.html')
    
@app.route('/helpPage')
def helpPage():
    return render_template('help.html')

Aname=''
Arole=''
@app.route('/login', methods=['GET',"POST"])
def loginValidate():
    if request.method == 'POST':
        email = request.form['email']
        passwd = request.form['passwd']
        cur = mysql.connection.cursor()
        rows = cur.execute('SELECT * FROM logindetails WHERE emailid=%s AND passwd=%s',(email,passwd))
        if rows > 0:
            details = cur.fetchall()
            global Aname, Arole
            Aname=details[0][1]
            Arole=details[0][3]
            if Arole == 'Principal':
                if (email in details[0][4]) and (passwd in details[0][5]):
                    return render_template('princi.html', name=Aname,role=Arole)
            elif Arole == 'Head':
                if (email in details[0][4]) and (passwd in details[0][5]):
                    return render_template('hod.html', name=Aname,role=Arole)
            elif Arole == 'Associate Professor':
                if (email in details[0][4]) and (passwd in details[0][5]):
                    return render_template('prof.html', name=Aname,role=Arole)
            elif Arole == 'Asst. Prof.':
                if (email in details[0][4]) and (passwd in details[0][5]):
                    return render_template('staffs.html', name=Aname,role=Arole)
        else:
            return render_template('login.html', msg='Invalid User')
        mysql.connection.commit()
        cur.close()
    else:
        return render_template('login.html')  

@app.route('/addTaskPage')
def addTaskPage():
    return render_template('AddTask.html', name=Aname, role=Arole)

@app.route('/taskAssign', methods=['GET','POST'])
def taskAssign():
    if request.method == 'POST':
        taskName = request.form['taskName']
        assignees = request.form.getlist('chck3')
        assignedby = request.form['assignedby']
        role = request.form['role']
        dateIn = str(request.form['datein'])
        dateOut = str(request.form['dateout'])
        priority = request.form['priority']
        comments = request.form['comment']

        print(assignees)
        # cur = mysql.connection.cursor()
        # cur.execute("INSERT INTO tasks(taskName,designation,assignees,assignedby,role,datein,dateout,priority,comments) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(taskName,desig,assignees,assignedby,role,dateIn,dateOut,priority,comments))
        # mysql.connection.commit()
        # cur.close()
        return 'Done'
    else:
        return 'Failed'

@app.route('/getNames', methods=['GET','POST'])
def getNames():
    if request.method == 'POST':
        dept = request.form.getlist('chck')
        desig = request.form.getlist('chck2')
        print(dept)
        cur = mysql.connection.cursor()
        for i in dept:
            for j in desig:
                rows = cur.execute('SELECT name FROM logindetails WHERE department=%s and designation=%s',(i,j))
                if rows > 0:
                    details = cur.fetchall()
                    return render_template('AddTask.html', name=Aname, role=Arole, infos=details, count=rows)       

@app.route('/taskByme')
def taskByme():
    cur = mysql.connection.cursor()
    rows = cur.execute('SELECT * FROM tasks WHERE assignedby=%s and role=%s',(Aname,Arole))
    if rows > 0:
        details = cur.fetchall()
        mysql.connection.commit()
        cur.close()
        return render_template('TaskByMe.html', infos=details, name=Aname, role=Arole)
    else:
        return render_template('TaskByMe.html', name=Aname, role=Arole, msg='No Entries yet :(')

@app.route('/editInfos')
def editInfos():
    return 'Done'

@app.route('/assignedTask')
def assignedTask():
    cur = mysql.connection.cursor()
    rows = cur.execute('SELECT * FROM tasks WHERE assignees=%s',(Aname,))
    if rows > 0:
        details = cur.fetchall()
        mysql.connection.commit()
        cur.close()
        return render_template('AssignedTask.html', infos=details, name=Aname)
    else:
        return render_template('AssignedTask.html',  name=Aname, msg='No tasks yet :)')
@app.route('/assignedView')
def assignedView():
    cur = mysql.connection.cursor()
    rows = cur.execute('SELECT * FROM tasks WHERE department=%s',('cse',))
    if rows > 0:
        details = cur.fetchall()
        mysql.connection.commit()
        cur.close()
        return render_template('AssignedView.html', infos=details, name=Aname,department='cse')
    else:
        return render_template('AssignedTask.html',  name=Aname, msg='No tasks yet :)')

@app.route('/changeStatus',methods=['POST','GET'])
def changeStatus():
    if request.method == 'POST':
        currentStatus = request.form['currentStatus']
        cur = mysql.connection.cursor()
        rows = cur.execute('UPDATE tasks SET status=%s WHERE assignees=%s',(currentStatus,Aname))
        mysql.connection.commit()
        cur.close()
        return assignedTask()
    else:
        return assignedTask()

@app.route('/dashboard')
def dashboard():
    cur = mysql.connection.cursor()
    row1 = cur.execute('SELECT * FROM tasks WHERE assignedby=%s',(Aname,))
    row2 = cur.execute('SELECT * FROM tasks WHERE assignees=%s',(Aname,))
    row3 = cur.execute('SELECT * FROM tasks WHERE assignees=%s and status="Completed"',(Aname,))
    row4 = cur.execute('SELECT * FROM tasks WHERE assignees=%s and status="In Progress"',(Aname,))
    mysql.connection.commit()
    cur.close()
    return render_template('Dashboard.html', name=Aname, tbm=row1, at=row2, cmp=row3, prg=row4)



if __name__ == '__main__':
    app.run(debug=True)