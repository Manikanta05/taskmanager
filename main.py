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

@app.route('/login', methods=['GET',"POST"])
def loginValidate():
    if request.method == 'POST':
        email = request.form['email']
        passwd = request.form['passwd']
        cur = mysql.connection.cursor()
        rows = cur.execute('SELECT * FROM logindetails WHERE emailid=%s AND passwd=%s',(email,passwd))
        if rows > 0:
            details = cur.fetchall()
            if details[0][3] == 'Principal':
                if (email in details[0][4]) and (passwd in details[0][5]):
                    return render_template('princi.html', name=details[0][1])
            elif details[0][3] == 'Head':
                if (email in details[0][4]) and (passwd in details[0][5]):
                    return render_template('hod.html', name=details[0][1])
            elif details[0][3] == 'Associate Professor':
                if (email in details[0][4]) and (passwd in details[0][5]):
                    return render_template('prof.html', name=details[0][1])
            elif details[0][3] == 'Asst. Prof.':
                if (email in details[0][4]) and (passwd in details[0][5]):
                    return render_template('staffs.html', name=details[0][1])
        else:
            return render_template('login.html', msg='Invalid User')
        mysql.connection.commit()
        cur.close()
    else:
        return render_template('login.html')  


if __name__ == '__main__':
    app.run(debug=True)

