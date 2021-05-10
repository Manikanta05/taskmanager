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

@app.route('/taskAssign', methods=['GET','POST'])
def taskAssign():
    if request.method == 'POST':
        taskName = request.form['taskName']
        desig = request.form['designation']
        assignees = request.form['assignees']
        assignedby = request.form['assignedby']
        role = request.form['role']
        dateIn = str(request.form['datein'])
        dateOut = str(request.form['dateout'])
        priority = request.form['priority']
        comments = request.form['comment']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO tasks(taskName,designation,assignees,assignedby,role,datein,dateout,priority,comments) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(taskName,desig,assignees,assignedby,role,dateIn,dateOut,priority,comments))
        mysql.connection.commit()
        cur.close()
        return 'Done'
    else:
        return 'Failed'


@app.route('/contact', methods=['GET','POST'])
def contact():
    if request.method == 'POST':
        namec = request.form['namec']
        emailc = request.form['emailc']
        phonec = request.form['phonec']
        subc = request.form['subc']
        msgc = request.form['msgc']

        cur1 = mysql.connection.cursor()
        cur1.execute("INSERT INTO contact(name,email,phone,subject,message) VALUES(%s,%s,%s,%s,%s)",(namec,emailc,phonec,subc,msgc))
        mysql.connection.commit()
        cur1.close()
        return 'Thank you for the feedback'
    else:
        return 'Failed'

@app.route('/taskByme')
def taskByme():
    cur = mysql.connection.cursor()
    rows = cur.execute('SELECT * FROM tasks WHERE assignedby=%s and role=%s',(Aname,Arole))
    if rows > 0:
        details = cur.fetchall()
        return render_template('TaskByMe.html', infos=details, name=Aname, role=Arole)
    else:
        return render_template('TaskByMe.html', name=Aname, role=Arole, msg='No Entries yet :(')

@app.route('/assignedTask')
def assignedTask():
    cur = mysql.connection.cursor()
    rows = cur.execute('SELECT * FROM tasks WHERE assignees=%s',(Aname,))
    if rows > 0:
        details = cur.fetchall()
        return render_template('AssignedTask.html', infos=details, name=Aname)
    else:
        return render_template('AssignedTask.html',  name=Aname, msg='No tasks yet :)')


if __name__ == '__main__':
    app.run(debug=True)
