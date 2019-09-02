from flask import Flask, render_template, request, redirect, flash, url_for
from flask_mysqldb import MySQL
import yaml
from forms import Search, AddEmployee


# Flask Instance creation
app=Flask(__name__)




# Loading 'yaml file' and importing variables
db = yaml.safe_load(open('db.yaml'))




app.config['SECRET_KEY']= db['secret_key']

#  Assigning yaml variale to config database
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

# Instance creation of MySQL database connecting to Flask
mysql=MySQL(app)





# fetches all records from Database 
@app.route('/user', methods=['GET','POST'])
def user():
    cur=mysql.connection.cursor()
    resultValue=cur.execute("Select * from EM_DETAILS")

    if resultValue>0:
        
        # fetch records from database
        userDetails = cur.fetchall()

        return render_template('user.html',userDetails=userDetails)
    return render_template('no_emp.html')    
    
# deletes a record from database
@app.route('/delete/<string:ename>', methods=['GET','POST'])
def delete(ename):
    cur=mysql.connection.cursor()
    cur.execute("DELETE FROM EM_DETAILS WHERE NAME= %s",(ename,))
    mysql.connection.commit()
    cur.close()
    return redirect('/user')

# adds an employee's details    
@ app.route("/addEmp", methods=['POST','GET'])
def addEmp():

    form = AddEmployee()

    if form.validate_on_submit():
        flash('Employee added successfully','success')
        redirect(url_for('addEmp')) 

    if request.method == 'POST':    
        # fetch 'form data' 
        userDetails = request.form
            
        # Initializing the values from input to variables
        ename=userDetails['name']
        desig=userDetails['designation']
        eaddress = userDetails['address']
        phone =  userDetails['phone']

        # Establishing Connection calling 'cursor' from 'connection class'
        cur=mysql.connection.cursor()

        # Executing the MySQL query
        cur.execute("INSERT INTO EM_DETAILS(NAME,DESIGNATION,ADDRESS,PHONE) VALUES(%s,%s,%s,%s)",(ename,desig,eaddress,phone))

        # Commiting changes into MySQL Data-Base
        mysql.connection.commit()

        # Closing the connection by closing cursor
        cur.close()

        return redirect('/addEmp')
    return render_template('addEmployee.html', form=form)

# seaching employee on Name, Designation or phone 
@ app.route("/", methods=['POST','GET'])
def search():
    form = Search()

    if request.method == 'POST':    
        # fetch 'form data' 
        userDetails = request.form
            
        # Initializing the values from input to variables
        search=userDetails['search']

        # Establishing Connection calling 'cursor' from 'connection class'
        cur=mysql.connection.cursor()

        # Executing the MySQL query
        value=cur.execute("SELECT * FROM EM_DETAILS WHERE NAME LIKE %s OR DESIGNATION LIKE %s OR PHONE LIKE %s",(search,search,search))
        
        userDetails=cur.fetchall()
        # Commiting changes into MySQL Data-Base
        mysql.connection.commit()

        # Closing the connection by closing cursor
        cur.close()

        if value==0 :
            return redirect('/')
        else:
            return render_template('searched.html',userDetails=userDetails)    
    return render_template('search.html', form=form)





# for activating debug mode
if __name__=='__main__':
    app.run(debug=True)



