

from flask import Flask,render_template, url_for,request, session
from flask_mysqldb import MySQL
import smtplib
from email.message import EmailMessage
from datetime import datetime


app = Flask(__name__)
app.secret_key = b'_1#j48e5%^15868\i?]/'

"""
app = Flask(__name__)
app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']=""
app.config['MYSQL_DB']="task_management"
"""
app.config['MYSQL_HOST']="EliteCoders.mysql.pythonanywhere-services.com"
app.config['MYSQL_USER']="EliteCoders"
app.config['MYSQL_PASSWORD']="elite1234"
app.config['MYSQL_DB']="EliteCoders$task_management"

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

@app.route('/teamPage')
def teamPage():
    return render_template('team.html')

@app.route('/resetpass', methods=['GET','POST'])
def resetpass():
    if request.method == 'POST':
        emailid=request.form['email']
        currpass=request.form['cpasswd']
        newpass=request.form['newpasswd']
        conpass=request.form['conpasswd']
        if newpass == conpass:
            cur = mysql.connection.cursor()
            rows = cur.execute('SELECT * FROM logindetails WHERE emailid=%s AND passwd=%s',(emailid,currpass))
            if rows>0:
                details=cur.fetchall()
                reset=cur.execute("UPDATE logindetails SET passwd=%s WHERE emailid=%s",(newpass,emailid))
                mysql.connection.commit()
                cur.close()
                return render_template('login.html', msg2="Password Changed Successfully :)")
            else:
                return render_template('login.html', msg="Couldn't reset your password, Try Again  :( ")
        else:
            return render_template('login.html', msg="Password doesn't match :( ")
    else:
        return render_template('login.html')


@app.route('/login',methods=['GET','POST'])
def loginValidate():
    if request.method == 'POST':
        email = request.form['email'].strip()
        passwd = request.form['passwd']
        cur = mysql.connection.cursor()
        rows = cur.execute('SELECT * FROM logindetails WHERE emailid=%s AND passwd=%s',(email,passwd))
        if rows > 0:
            details = cur.fetchall()
            Aname=details[0][1]
            Arole=details[0][3]
            if 'username' in session:
                if Arole == 'Principal':
                    if (email in details[0][4]) and (passwd in details[0][5]):
                        # print(str(session['username']) +' created already')
                        return render_template('princi.html', name=Aname,role=Arole)
                elif Arole == 'JD':
                    if (email in details[0][4]) and (passwd in details[0][5]):
                        totalTasks=cur.execute("SELECT * FROM tasks")
                        assignedTasks=cur.execute("SELECT * FROM tasks WHERE status='Assigned'")
                        completedTasks=cur.execute("SELECT * FROM tasks WHERE status='Completed'")
                        inprogressTasks=cur.execute("SELECT * FROM tasks WHERE status='In Progress'")
                        return render_template('jd.html',totalTasks=totalTasks,assignedTasks=assignedTasks,completedTasks=completedTasks,inprogressTasks=inprogressTasks,name=Aname,role=Arole)
                elif Arole == 'Head':
                    if (email in details[0][4]) and (passwd in details[0][5]):
                        # print(str(session['username']) +' created already')
                        return render_template('hod.html', name=Aname,role=Arole)
                elif Arole == 'Professor':
                    if (email in details[0][4]) and (passwd in details[0][5]):
                        return render_template('prof.html', name=Aname,role=Arole)
                elif Arole == 'Associate Professor':
                    if (email in details[0][4]) and (passwd in details[0][5]):
                        return render_template('prof.html', name=Aname,role=Arole)
                elif Arole == 'Asst. Prof.':
                    if (email in details[0][4]) and (passwd in details[0][5]):
                        return render_template('staffs.html', name=Aname,role=Arole)
                elif Arole == 'System Analyst' or Arole =='Foreman'or Arole =='Programmer' or Arole =='Instructor' or Arole =='Lab Helper' or Arole =='Attender' or Arole =='Helper'or Arole =='Lab Instructor':
                    if (email in details[0][4]) and (passwd in details[0][5]):
                        return render_template('staffsnt.html', name=Aname,role=Arole)
            else:
                session['username'] = details[0][1]
                # print(str(session['username']) +' created now')
                if Arole == 'Principal':
                    if (email in details[0][4]) and (passwd in details[0][5]):
                        return render_template('princi.html', name=Aname,role=Arole)
                elif Arole == 'JD':
                    if (email in details[0][4]) and (passwd in details[0][5]):
                        totalTasks=cur.execute("SELECT * FROM tasks")
                        assignedTasks=cur.execute("SELECT * FROM tasks WHERE status='Assigned'")
                        completedTasks=cur.execute("SELECT * FROM tasks WHERE status='Completed'")
                        inprogressTasks=cur.execute("SELECT * FROM tasks WHERE status='In Progress'")
                        return render_template('jd.html',totalTasks=totalTasks,assignedTasks=assignedTasks,completedTasks=completedTasks,inprogressTasks=inprogressTasks,name=Aname,role=Arole)
                elif Arole == 'Head':
                    if (email in details[0][4]) and (passwd in details[0][5]):
                        return render_template('hod.html', name=Aname,role=Arole)
                elif Arole == 'Professor':
                    if (email in details[0][4]) and (passwd in details[0][5]):
                        return render_template('prof.html', name=Aname,role=Arole)
                elif Arole == 'Associate Professor':
                    if (email in details[0][4]) and (passwd in details[0][5]):
                        return render_template('prof.html', name=Aname,role=Arole)
                elif Arole == 'Asst. Prof.':
                    if (email in details[0][4]) and (passwd in details[0][5]):
                        return render_template('staffs.html', name=Aname,role=Arole)
                elif Arole == 'System Analyst' or Arole =='Foreman'or Arole =='Programmer' or Arole =='Instructor' or Arole =='Lab Helper' or Arole =='Attender' or Arole =='Helper'or Arole =='Lab Instructor':
                    if (email in details[0][4]) and (passwd in details[0][5]):
                        return render_template('staffsnt.html', name=Aname,role=Arole)
        else:
            return render_template('login.html', msg='Invalid Email-id or Password :( ')
        mysql.connection.commit()
        cur.close()
    else:
       return render_template('login.html', msg='Please Login To Proceed ')


@app.route('/addTaskPage')
def addTaskPage():
    if 'username' in session:
        user = session['username']
        # print(user)
        cur = mysql.connection.cursor()
        rows = cur.execute('SELECT * FROM logindetails WHERE name=%s',(user,))
        if rows > 0:
            details = cur.fetchall()
            Aname=details[0][1]
            Arole=details[0][3]
            # print(Aname)
            # print(Arole)
            return render_template('AddTask.html', name=Aname, role=Arole)
    else:
        return render_template('login.html', msg='Please Login To Proceed ')


@app.route('/taskAssign', methods=['GET','POST'])
def taskAssign():
    if request.method == 'POST':
        if 'username' in session:
            user = session['username']
            # print(user)
            cur = mysql.connection.cursor()
            rows = cur.execute('SELECT * FROM logindetails WHERE name=%s',(user,))
            try:
                if rows > 0:
                    details = cur.fetchall()
                    Aname=details[0][1]
                    Arole=details[0][3]

                    taskType = request.form.getlist('taskType')
                    taskName = request.form['taskName']
                    assignees = request.form.getlist('chck3')
                    assignedby = request.form['assignedby']
                    role = request.form['role']
                    dateIn = str(request.form['datein'])
                    dateOut = str(request.form['dateout'])
                    priority = request.form['priority']
                    comments = request.form['comment']

                    tt=""
                    # print(taskType,taskType[0])
                    if taskType[0]=="yes":
                        tt="Group Task"
                    else:
                        tt="Individual Task"
                    contacts = []

                    if len(assignees) == 1 :
                        n=cur.execute('SELECT department,designation,emailid FROM logindetails where name=%s',(assignees[0],))
                        depart=cur.fetchall()
                        contacts.append(depart[0][2])
                        cur.execute("INSERT INTO tasks(taskName,assignees,designation,groupTask,assignedby,role,dept,datein,dateout,priority,comments) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(taskName,assignees[0],depart[0][1],taskType,assignedby,role,depart[0][0],dateIn,dateOut,priority,comments))
                        mysql.connection.commit()
                    elif len(assignees) > 1:
                        for i in assignees:
                            n=cur.execute('SELECT department,designation,emailid FROM logindetails where name=%s',(i,))
                            depart=cur.fetchall()
                            contacts.append(depart[0][2])
                            cur.execute("INSERT INTO tasks(taskName,assignees,designation,groupTask,assignedby,role,dept,datein,dateout,priority,comments) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(taskName,i,depart[0][1],taskType,assignedby,role,depart[0][0],dateIn,dateOut,priority,comments))
                            mysql.connection.commit()
                    else:
                        return render_template('AddTask.html', name=Aname, role=Arole, msg='Select atleast 1 Assignee', color='danger')
                    cur.close()

                    EMAIL_ADDRESS = "elitecoders.jss@gmail.com"
                    msg = EmailMessage()
                    msg['Subject'] = 'New task has been assigned!'
                    msg['From'] = EMAIL_ADDRESS
                    msg['To'] = contacts
                    dt_string = datetime.now().strftime("%m %B,%Y %H:%M:%S")
                    msg.set_content('New task has been assigned!')
                    msg.add_alternative("""\
                    <!DOCTYPE html>
                    <html>
                        <body>
                         <a href="https://elitecoders.pythonanywhere.com/" style="text-decoration: none;"> <h1 style="color:#3737b3;font-size:70px; font-family:'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif">Task Manager</h1></a>
                    <h2 style="font-size:30px;">
                    <mark>Taskname : """+taskName.upper()+"""</mark></h2>
                    <h3 style="color:#500050;">
                    Task Type : """+tt+"""<br>
                    Priority : """+priority.upper()+"""<br>
                    Assigned By : """+assignedby+"""<br>
                    Assigned Date : """+dateIn+"""<br>
                    Due Date : """+dateOut+"""<br>
                    Comments : """+comments+"""
                    </h3>
                    <h4 class="text-muted">"""+dt_string+"""</h4>
                        </body>
                    </html>
                    """, subtype='html')
                    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
                        smtp.login('elitecoders.jss@gmail.com','elite1234')
                        smtp.send_message(msg)

                    return render_template('AddTask.html', name=Aname, role=Arole, msg='Task Assigned successfully :)', color='success')
                else:
                    return render_template('AddTask.html', name=Aname, role=Arole, msg='Failed :(', color='danger')


            except:
                 return render_template('AddTask.html', name=Aname, role=Arole, msg='Task Already exists :(', color='danger')

    else:
        return render_template('login.html', msg='Please Login To Proceed ')

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
        EMAIL_ADDRESS = "elitecoders.jss@gmail.com"
        msg = EmailMessage()
        msg['Subject'] = 'Support!'
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = EMAIL_ADDRESS
        dt_string = datetime.now().strftime("%m %B,%Y %H:%M:%S")
        msg.set_content('Support!')
        msg.add_alternative("""\
        <!DOCTYPE html>
        <html>
        <body>
        <a href="https://elitecoders.pythonanywhere.com/" style="text-decoration:none" target="blank">
        <h1 style="color:#3737b3;font-size:80px; font-family:'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif">Task Manager</h1></a>
        <h2 style="font-size:30px;">
        <mark>Subject : """+subc.upper()+"""</mark></h2>
        <h3 style="color:#500050;">
        Name : """+namec+"""<br>
        Email : """+emailc+"""<br>
        Message : """+msgc+"""<br>
        </h3>
        <h4 class="text-muted">"""+dt_string+"""</h4>
        </body>
        </html>
        """, subtype='html')
        with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
            smtp.login('elitecoders.jss@gmail.com','elite1234')
            smtp.send_message(msg)
        return goBack()
    else:
        return render_template('login.html',msg="Please Login To Proceed")

@app.route('/getNames', methods=['GET','POST'])
def getNames():
    if request.method == 'POST':
        if 'username' in session:
            user = session['username']
            # print(user)
            cur = mysql.connection.cursor()
            rows = cur.execute('SELECT * FROM logindetails WHERE name=%s',(user,))
            if rows > 0:
                details = cur.fetchall()
                Aname=details[0][1]
                Arole=details[0][3]

                dept = request.form.getlist('chck')
                desig = request.form.getlist('chck2')
                listall=[]
                depList= dept
                for i in dept:
                    for j in desig:
                        rows = cur.execute('SELECT name,department FROM logindetails WHERE department=%s and designation=%s',(i,j))
                        details = cur.fetchall()
                        listall.append(details)
                return render_template('AddTask.html', name=Aname, role=Arole, infos=listall, count=len(listall))
    else:
        return render_template('login.html', msg='Please Login To Proceed ')


@app.route('/taskByme')
def taskByme():
    if 'username' in session:
            user = session['username']
            # print(user)
            cur = mysql.connection.cursor()
            rows = cur.execute('SELECT * FROM logindetails WHERE name=%s',(user,))
            if rows > 0:
                details = cur.fetchall()
                Aname=details[0][1]
                Arole=details[0][3]

                rows = cur.execute('SELECT * FROM tasks WHERE assignedby=%s and role=%s and groupTask="no" and status<>"Deleted"',(Aname,Arole))
                # print(rows,Aname,Arole)
                if rows > 0:
                    details = cur.fetchall()
                    mysql.connection.commit()
                    cur.close()
                    return render_template('TaskByMe.html', infos=details, name=Aname, role=Arole)
                else:
                    return render_template('TaskByMe.html', name=Aname, role=Arole, msg='No Entries yet :(')
    else:
        return render_template('login.html', msg='Please Login To Proceed ')

@app.route('/taskBymeGroup')
def taskBymeGroup():
    if 'username' in session:
            user = session['username']
            # print(user)
            cur = mysql.connection.cursor()
            rows = cur.execute('SELECT * FROM logindetails WHERE name=%s',(user,))
            if rows > 0:
                details = cur.fetchall()
                Aname=details[0][1]
                Arole=details[0][3]

                rows = cur.execute('SELECT * FROM tasks WHERE assignedby=%s and role=%s and status<>"Deleted" and groupTask="yes" ORDER BY taskName DESC',(Aname,Arole))
                if rows > 0:
                    details = cur.fetchall()
                    mysql.connection.commit()
                    cur.close()
                    return render_template('taskBymeGroup.html', infos=details, name=Aname, role=Arole)
                else:
                    return render_template('taskBymeGroup.html', name=Aname, role=Arole, msg='No Entries yet :(')
    else:
        return render_template('login.html', msg='Please Login To Proceed ')

@app.route('/assignedTask')
def assignedTask():
    if 'username' in session:
            user = session['username']
            # print(user)
            cur = mysql.connection.cursor()
            rows = cur.execute('SELECT * FROM logindetails WHERE name=%s',(user,))
            if rows > 0:
                details = cur.fetchall()
                Aname=details[0][1]
                Arole=details[0][3]

                rows = cur.execute('SELECT * FROM tasks WHERE assignees=%s and status<>"Deleted"',(Aname,))
                if rows > 0:
                    details = cur.fetchall()
                    mysql.connection.commit()
                    cur.close()
                    return render_template('AssignedTask.html', infos=details, name=Aname)
                else:
                    return render_template('AssignedTask.html',  name=Aname, msg='No tasks yet :)')
    else:
        return render_template('login.html', msg='Please Login To Proceed ')

@app.route('/changeStatus',methods=['POST','GET'])
def changeStatus():
    if request.method == 'POST':
        if 'username' in session:
            user = session['username']
            # print(user)
            cur = mysql.connection.cursor()
            rows = cur.execute('SELECT * FROM logindetails WHERE name=%s',(user,))
            if rows > 0:
                details = cur.fetchall()
                Aname=details[0][1]
                Arole=details[0][3]

                try:
                    taskName = request.form['taskName']
                    currentStatus = request.form['currentStatus']
                    turnin = request.form['turnin']
                    cur = mysql.connection.cursor()
                    rows = cur.execute('UPDATE tasks SET status=%s, turnedin=%s WHERE assignees=%s AND taskName=%s',(currentStatus,turnin,Aname,taskName))
                    mysql.connection.commit()
                    cur.close()
                    return assignedTask()
                except:
                    return render_template('AssignedTask.html',name=Aname, msg='Please select Status and Turn-in date')
    else:
        return assignedTask()

@app.route('/dashboard')
def dashboard():
    if 'username' in session:
            user = session['username']
            # print(user)
            cur = mysql.connection.cursor()
            rows = cur.execute('SELECT * FROM logindetails WHERE name=%s',(user,))
            if rows > 0:
                details = cur.fetchall()
                Aname=details[0][1]
                Arole=details[0][3]

                row1 = cur.execute('SELECT distinct taskName FROM tasks WHERE assignedby=%s',(Aname,))
                row2 = cur.execute('SELECT * FROM tasks WHERE assignees=%s',(Aname,))
                row3 = cur.execute('SELECT * FROM tasks WHERE assignees=%s and status="Completed"',(Aname,))
                row4 = cur.execute('SELECT * FROM tasks WHERE assignees=%s and status="In Progress"',(Aname,))
                mysql.connection.commit()
                cur.close()
                return render_template('Dashboard.html', name=Aname, tbm=row1, at=row2, cmp=row3, prg=row4)
    else:
        return render_template('login.html', msg='Please Login To Proceed ')

# #For assignee
@app.route('/remarkview',methods=['POST','GET'])
def remarkview():
    if request.method == 'POST':
        if 'username' in session:
            user = session['username']
            # print(user)
            cur = mysql.connection.cursor()
            rows = cur.execute('SELECT * FROM logindetails WHERE name=%s',(user,))
            if rows > 0:
                details = cur.fetchall()
                Aname=details[0][1]
                Arole=details[0][3]

                tid=request.form['id']
                tn=request.form['taskName']
                tass=request.form['assignees']
                tdes=request.form['designation']
                tassb=request.form['assignedby']
                role=request.form['role']
                dept=request.form['dept']
                gt=request.form['groupTask']
                cur = mysql.connection.cursor()
                if gt=="yes":
                    tts=cur.execute('SELECT * FROM remarks WHERE taskName=%s and assignedby=%s and role=%s order by time desc',(tn,tassb,role,))
                else:
                    tts=cur.execute('SELECT * FROM remarks WHERE assignees=%s and taskName=%s and assignedby=%s and role=%s and dept=%s order by time desc',(tass,tn,tassb,role,dept,))
                details1=None
                if tts > 0:
                    details1 = cur.fetchall()
                return render_template('remarkview.html',tid=tid,tn=tn,tass=tass,tdes=tdes,tassb=tassb,role=role,dept=dept,name=Aname,infos=details1,msg="No remarks yet")
    else:
        return render_template('login.html', msg='Please Login To Proceed ')


# #for assigned person
@app.route('/remarkview1',methods=['POST','GET'])
def remarkview1():
    if request.method == 'POST':
        if 'username' in session:
            user = session['username']
            # print(user)
            cur = mysql.connection.cursor()
            rows = cur.execute('SELECT * FROM logindetails WHERE name=%s',(user,))
            if rows > 0:
                details = cur.fetchall()
                Aname=details[0][1]
                Arole=details[0][3]

                tid=request.form['id']
                tn=request.form['taskName']
                tass=request.form['assignees']
                tdes=request.form['designation']
                tassb=request.form['assignedby']
                role=request.form['role']
                dept=request.form['dept']
                gt=request.form['groupTask']
                cur = mysql.connection.cursor()
                if gt=="yes":
                    tts=cur.execute('SELECT * FROM remarks WHERE taskName=%s and assignedby=%s and role=%s order by time desc',(tn,tassb,role,))
                else:
                    tts=cur.execute('SELECT * FROM remarks WHERE assignees=%s and taskName=%s and assignedby=%s and role=%s and dept=%s order by time desc',(tass,tn,tassb,role,dept,))
                details1=None
                if tts > 0:
                    details1 = cur.fetchall()
                return render_template('remarkview1.html',tid=tid,tn=tn,tass=tass,tdes=tdes,tassb=tassb,role=role,dept=dept,name=Aname,infos=details1,msg="No remarks yet")
    else:
        return render_template('login.html', msg='Please Login To Proceed ')

@app.route('/remarks',methods=['POST','GET'])
def remarks():
    if request.method == 'POST':
        if 'username' in session:
            user = session['username']
            # print(user)
            cur = mysql.connection.cursor()
            rows = cur.execute('SELECT * FROM logindetails WHERE name=%s',(user,))
            if rows > 0:
                details = cur.fetchall()
                Aname=details[0][1]
                Arole=details[0][3]

                tid=request.form['id']
                tn=request.form['taskName']
                tass=request.form['assignees']
                tdes=request.form['designation']
                tassb=request.form['assignedby']
                role=request.form['role']
                dept=request.form['dept']
                rem=request.form['remarks']
                cur = mysql.connection.cursor()
                tts=cur.execute('insert into remarks (taskname,assignees,designation,assignedby,role,dept,remarks,name) values(%s,%s,%s,%s,%s,%s,%s,%s)',(tn,tass,tdes,tassb,role,dept,rem,tass))
                mysql.connection.commit()
                cur.close()
                return assignedTask()
    else:
        return render_template('login.html', msg='Please Login To Proceed ')

@app.route('/remarks1',methods=['POST','GET'])
def remarks1():
    if request.method == 'POST':
        if 'username' in session:
            user = session['username']
            # print(user)
            cur = mysql.connection.cursor()
            rows = cur.execute('SELECT * FROM logindetails WHERE name=%s',(user,))
            if rows > 0:
                details = cur.fetchall()
                Aname=details[0][1]
                Arole=details[0][3]

                tid=request.form['id']
                tn=request.form['taskName']
                tass=request.form['assignees']
                tdes=request.form['designation']
                tassb=request.form['assignedby']
                role=request.form['role']
                dept=request.form['dept']
                rem=request.form['remarks']
                cur = mysql.connection.cursor()
                tts=cur.execute('insert into remarks (taskname,assignees,designation,assignedby,role,dept,remarks,name) values(%s,%s,%s,%s,%s,%s,%s,%s)',(tn,tass,tdes,tassb,role,dept,rem,Aname))
                mysql.connection.commit()
                cur.close()
                return goBack()
    else:
        return render_template('login.html', msg='Please Login To Proceed ')

# #principaldashboard
@app.route('/pdash',methods=['POST','GET'])
def pdash():
    if request.method == 'POST':
        if 'username' in session:
            user = session['username']
            # print(user)
            cur = mysql.connection.cursor()
            rows = cur.execute('SELECT * FROM logindetails WHERE name=%s',(user,))
            if rows > 0:
                details = cur.fetchall()
                Aname=details[0][1]
                Arole=details[0][3]

                dept=request.form['dept']
                tts=cur.execute('SELECT * FROM tasks WHERE dept=%s AND status<>"Deleted"',(dept,))
                hods=cur.execute('SELECT * FROM tasks WHERE dept=%s AND designation="Head" AND status<>"Deleted"',(dept,))
                pts=cur.execute('SELECT * FROM tasks WHERE dept=%s AND designation="Professor" AND status<>"Deleted"',(dept,))
                aps=cur.execute('SELECT * FROM tasks WHERE dept=%s AND designation="Associate Professor" AND status<>"Deleted"',(dept,))
                assts=cur.execute('SELECT * FROM tasks WHERE dept=%s AND designation="Asst. Prof." AND status<>"Deleted"',(dept,))
                asnt1=cur.execute('SELECT * FROM tasks WHERE dept=%s and status="Assigned" AND status<>"Deleted"',(dept,))
                inpt1 = cur.execute('SELECT * FROM tasks WHERE status="In Progress" AND dept=%s AND status<>"Deleted"',(dept,))
                ct1 = cur.execute('SELECT * FROM tasks WHERE status="Completed" AND dept=%s AND status<>"Deleted"',(dept,))
                ot1 = cur.execute('SELECT * FROM tasks WHERE dept=%s and dateout<CURRENT_DATE() and status not in( "Completed")',(dept,))

                details1=details2=details3=details4=details5=msg1=msg2=msg3=msg4=msg5=None
                row1 = cur.execute('SELECT * FROM tasks WHERE dept=%s AND status<>"Deleted"',(dept,))
                if row1 > 0:
                    details1 = cur.fetchall()
                else:
                    msg1='No tasks yet'
                row2 = cur.execute('SELECT * FROM tasks WHERE designation="Head"and dept=%s AND status<>"Deleted"',(dept,))
                if row2 > 0:
                    details2 = cur.fetchall()
                else:
                    msg2='No tasks yet'
                row3 = cur.execute('SELECT * FROM tasks WHERE designation="Professor"and dept=%s AND status<>"Deleted"',(dept,))
                if row3 > 0:
                    details3 = cur.fetchall()
                else:
                    msg3='No tasks yet'
                row4 = cur.execute('SELECT * FROM tasks WHERE designation="Associate Professor" and dept=%s AND status<>"Deleted"',(dept,))
                if row4 > 0:
                    details4 = cur.fetchall()
                else:
                    msg4='No tasks yet'
                row5 = cur.execute('SELECT * FROM tasks WHERE designation="Asst. Prof." and dept=%s AND status<>"Deleted"',(dept,))
                if row5 > 0:
                    details5 = cur.fetchall()
                else:
                    msg5='No tasks yet'

                mysql.connection.commit()
                cur.close()
                return render_template('princi_dash.html',role=Arole, name=Aname,dept=dept,tt=tts,hod=hods,pt=pts,ap=aps,assts=assts,asnt=asnt1,inpt=inpt1,ct=ct1,ot=ot1,infos1=details1,infos2=details2,infos3=details3,infos4=details4,infos5=details5,msg1=msg1,msg2=msg2,msg3=msg3,msg4=msg4,msg5=msg5)
    elif request.method == 'GET':
        if 'username' in session:
            user = session['username']
            print(user)
            cur = mysql.connection.cursor()
            rows = cur.execute('SELECT * FROM logindetails WHERE name=%s',(user,))
            if rows > 0:
                details = cur.fetchall()
                Aname=details[0][1]
                Arole=details[0][3]
                Adept=details[0][2]
                dept=Adept

                tts=cur.execute('SELECT * FROM tasks WHERE dept=%s AND status<>"Deleted"',(dept,))
                hods=cur.execute('SELECT * FROM tasks WHERE dept=%s AND designation="Head" AND status<>"Deleted"',(dept,))
                pts=cur.execute('SELECT * FROM tasks WHERE dept=%s AND designation="Professor" AND status<>"Deleted"',(dept,))
                aps=cur.execute('SELECT * FROM tasks WHERE dept=%s AND designation="Associate Professor" AND status<>"Deleted"',(dept,))
                assts=cur.execute('SELECT * FROM tasks WHERE dept=%s AND designation="Asst. Prof." AND status<>"Deleted"',(dept,))
                asnt1=cur.execute('SELECT * FROM tasks WHERE dept=%s and status="Assigned" AND status<>"Deleted"',(dept,))
                inpt1 = cur.execute('SELECT * FROM tasks WHERE status="In Progress" AND dept=%s AND status<>"Deleted"',(dept,))
                ct1 = cur.execute('SELECT * FROM tasks WHERE status="Completed" AND dept=%s AND status<>"Deleted"',(dept,))
                ot1 = cur.execute('SELECT * FROM tasks WHERE dept=%s and dateout<CURRENT_DATE() and status not in( "Completed")',(dept,))

                details1=details2=details3=details4=details5=msg1=msg2=msg3=msg4=msg5=None
                row1 = cur.execute('SELECT * FROM tasks WHERE dept=%s AND status<>"Deleted"',(dept,))
                if row1 > 0:
                    details1 = cur.fetchall()
                else:
                    msg1='No tasks yet'
                row2 = cur.execute('SELECT * FROM tasks WHERE designation="Head"and dept=%s AND status<>"Deleted"',(dept,))
                if row2 > 0:
                    details2 = cur.fetchall()
                else:
                    msg2='No tasks yet'
                row3 = cur.execute('SELECT * FROM tasks WHERE designation="Professor"and dept=%s AND status<>"Deleted"',(dept,))
                if row3 > 0:
                    details3 = cur.fetchall()
                else:
                    msg3='No tasks yet'
                row4 = cur.execute('SELECT * FROM tasks WHERE designation="Associate Professor" and dept=%s AND status<>"Deleted"',(dept,))
                if row4 > 0:
                    details4 = cur.fetchall()
                else:
                    msg4='No tasks yet'
                row5 = cur.execute('SELECT * FROM tasks WHERE designation="Asst. Prof." and dept=%s AND status<>"Deleted"',(dept,))
                if row5 > 0:
                    details5 = cur.fetchall()
                else:
                    msg5='No tasks yet'

                mysql.connection.commit()
                cur.close()

                return render_template('DepartmentDashboard.html',role=Arole, name=Aname,dept=dept,tt=tts,hod=hods,pt=pts,ap=aps,assts=assts,asnt=asnt1,inpt=inpt1,ct=ct1,ot=ot1,infos1=details1,infos2=details2,infos3=details3,infos4=details4,infos5=details5,msg1=msg1,msg2=msg2,msg3=msg3,msg4=msg4,msg5=msg5)

    else:
        return render_template('login.html', msg='Please Login To Proceed ')

@app.route('/deptdashboard')
def deptdashboard():
    if 'username' in session:
            user = session['username']
            # print(user)
            cur = mysql.connection.cursor()
            rows = cur.execute('SELECT * FROM logindetails WHERE name=%s',(user,))
            if rows > 0:
                details = cur.fetchall()
                Aname=details[0][1]
                Arole=details[0][3]
                Adept=details[0][2]

                row1 = cur.execute('SELECT * FROM tasks WHERE dept=%s AND status<>"Deleted" ',(Adept,))
                row2 = cur.execute('SELECT * FROM tasks WHERE dept=%s AND designation="Head" AND status<>"Deleted"',(Adept,))
                row3 = cur.execute('SELECT * FROM tasks WHERE dept=%s AND designation="Professor" AND status<>"Deleted"',(Adept,))
                row4 = cur.execute('SELECT * FROM tasks WHERE dept=%s AND designation="Associate Professor" AND status<>"Deleted"',(Adept,))
                row5 = cur.execute('SELECT * FROM tasks WHERE dept=%s AND designation="Asst. Prof." AND status<>"Deleted"',(Adept,))

                row6 = cur.execute('SELECT * FROM tasks WHERE status="Completed" AND dept=%s AND designation="Head" AND status<>"Deleted"',(Adept,))
                row7 = cur.execute('SELECT * FROM tasks WHERE status="Assigned" AND dept=%s AND designation="Head" AND status<>"Deleted"',(Adept,))
                row8 = cur.execute('SELECT * FROM tasks WHERE status="In Progress" AND dept=%s AND designation="Head" AND status<>"Deleted"',(Adept,))

                row9 = cur.execute('SELECT * FROM tasks WHERE status="Completed" AND dept=%s AND designation="Professor" AND status<>"Deleted"',(Adept,))
                row10 = cur.execute('SELECT * FROM tasks WHERE status="Assigned" AND dept=%s AND designation="Professor" AND status<>"Deleted"',(Adept,))
                row11 = cur.execute('SELECT * FROM tasks WHERE status="In Progress" AND dept=%s AND designation="Professor" AND status<>"Deleted"',(Adept,))

                row12 = cur.execute('SELECT * FROM tasks WHERE status="Completed" AND dept=%s AND designation="Associate Professor" AND status<>"Deleted"',(Adept,))
                row13 = cur.execute('SELECT * FROM tasks WHERE status="Assigned" AND dept=%s AND designation="Associate Professor" AND status<>"Deleted"',(Adept,))
                row14 = cur.execute('SELECT * FROM tasks WHERE status="In Progress" AND dept=%s AND designation="Associate Professor" AND status<>"Deleted"',(Adept,))

                row15 = cur.execute('SELECT * FROM tasks WHERE status="Completed" AND dept=%s AND designation="Asst. Prof." AND status<>"Deleted"',(Adept,))
                row16 = cur.execute('SELECT * FROM tasks WHERE status="Assigned" AND dept=%s AND designation="Asst. Prof." AND status<>"Deleted"',(Adept,))
                row17 = cur.execute('SELECT * FROM tasks WHERE status="In Progress" AND dept=%s AND designation="Asst. Prof." AND status<>"Deleted"',(Adept,))

                mysql.connection.commit()
                cur.close()
                return render_template('DepartmentDashboard.html', tt=row1, th=row2, tp=row3, tap=row4, tasp=row5, tch=row6, tah=row7, tph=row8, tcp=row9, tapp=row10, tpp=row11, tcap=row12, taap=row13, tpap=row14, tcasp=row15, taasp=row16, tpasp=row17)
    else:
        return render_template('login.html', msg='Please Login To Proceed ')

@app.route('/deleteTask', methods=['GET','POST'])
def deleteTask():
    if request.method == 'POST':
        if 'username' in session:
            user = session['username']
            # print(user)
            cur = mysql.connection.cursor()
            rows = cur.execute('SELECT * FROM logindetails WHERE name=%s',(user,))
            if rows > 0:
                details = cur.fetchall()
                Aname=details[0][1]
                Arole=details[0][3]

                taskName = request.form['taskName']
                rows = cur.execute('SELECT taskName FROM tasks WHERE taskName=%s',(taskName,))
                if rows>0:
                    delte = cur.execute("UPDATE tasks SET status='Deleted' WHERE taskName=%s",(taskName,))
                    mysql.connection.commit()
                    cur.close()
                    return taskByme()
                else:
                    return "Task doesn't exist :("
    else:
        return render_template('login.html', msg='Please Login To Proceed ')

@app.route('/goBack')
def goBack():
    if 'username' in session:
        user = session['username']
        print(user)
        cur = mysql.connection.cursor()
        rows = cur.execute('SELECT * FROM logindetails WHERE name=%s',(user,))
        if rows > 0:
            details = cur.fetchall()
            Aname=details[0][1]
            Arole=details[0][3]
            if Arole == 'Principal':
                return render_template('princi.html', name=Aname,role=Arole)
            elif Arole == 'JD':
                cur = mysql.connection.cursor()
                totalTasks=cur.execute("SELECT * FROM tasks")
                assignedTasks=cur.execute("SELECT * FROM tasks WHERE status='Assigned'")
                completedTasks=cur.execute("SELECT * FROM tasks WHERE status='Completed'")
                inprogressTasks=cur.execute("SELECT * FROM tasks WHERE status='In Progress'")
                return render_template('jd.html',totalTasks=totalTasks,assignedTasks=assignedTasks,completedTasks=completedTasks,inprogressTasks=inprogressTasks,name=Aname,role=Arole)
            elif Arole == 'Head':
                return render_template('hod.html', name=Aname,role=Arole)
            elif Arole == 'Professor':
                return render_template('prof.html', name=Aname,role=Arole)
            elif Arole == 'Associate Professor':
                return render_template('prof.html', name=Aname,role=Arole)
            elif Arole == 'Asst. Prof.':
                return render_template('staffs.html', name=Aname,role=Arole)
            elif Arole == 'System Analyst' or Arole =='Foreman'or Arole =='Programmer' or Arole =='Instructor' or Arole =='Lab Helper' or Arole =='Attender' or Arole =='Helper'or Arole =='Lab Instructor':
                return render_template('staffsnt.html', name=Aname,role=Arole)
            else:
                return render_template('Error.html')
        else:
            return render_template('Error.html')
    else:
        return render_template('login.html', msg='Please Login To Proceed ')

@app.route('/logout')
def logout():
    if 'username' in session:
        print('logged out '+str(session['username']))
        session.pop('username', None)
        return render_template('index.html')
    else:
        return render_template('login.html', msg='Please Login To Proceed ')

if __name__ == '__main__':
    app.run(debug=True)
