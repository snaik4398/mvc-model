from app import app
from flask import render_template

from cgitb import html
import collections
from flask import Flask, redirect, url_for, render_template, request, session
# import pymongo

from flask_mysqldb import MySQL
import MySQLdb.cursors
# import re
import random

# ______________________________________________________
# for mysql
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'sqluser'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'pymsql'

# ____________________________________________________
mysql = MySQL(app)

# welcome page


l=list()

   
 
    # return ' Name: '+pname+'   Email: '+pemail+'   Gender: ' + pgender+' D.O.B: '+pdob+'  PIN: '+ppin+' '
    # return ''' Name: '+{{pname}}}+'   Email: '+pemail+'   Gender: ' + pgender+' D.O.B: '+pdob+'  PIN: '+ppin+' '''

# to display data in all the html PAGES


@app.context_processor
def context_processor():
    # if we directly return the value then its showing not definedName=pname,Email=pemail,Gender=pgender,Dob=pdob,PIN=ppin
    return dict(lo=l)


def home():
    # when we are trying to re render it its showing method not allowed
    return redirect(url_for('welcome'))

    # return redirect('/')



def makeadharglob(adh):
    global adhar
    adhar = adh


def making_global_info(name, mail, pin, gender, dob, id):

    global pemail, pdob, pgender, ppin, pname, gpid
    pname = name
    pemail = mail
    pdob = dob
    pgender = gender
    ppin = pin
    gpid = id
 


def randomPat_id(digits):
    lower = 10**(digits-1)
    upper = 10**digits - 1
    return random.randint(lower, upper)


# Result checker submit html page
@app.route('/signup', methods=['POST', 'GET'])
def signup():
    msg = " "
    # creating the local variable inside the function to fetch the values from the form
    pat_id=" "
    name1 = " "
    email1 = " "
    gen1 = " "
    phno = " "
    adhar = " "
    pin = " "
    dob = " "
    sc = " "
    res = " "

    # in the form we mention method=POST so the request object need to go by the post methods
    if request.method == 'POST':
        pat_id= str(randomPat_id(14))
        fnm = request.form['fname']
        fname=fnm.strip()
        if len(fname) >=20:
            return render_template('signup.html',error='name field can handel upto 20 character')


        # for and other spl character
        if fname.isalpha() or fname.count(" ")==2 or fname.count(" ")==1:
            print("should continue")
        else:
            return render_template('signup.html',error='enter correct name in the name field')
        # for single space 
        if fname=="" or fname==" " or fname=="  " :
            print("hello for fname ")
            return render_template('signup.html',error='enter correct name in first name  field  it can not be blank space only')
        lnm=request.form['lname']
        lname=lnm.strip()
        if lname=="" or lname==" " or lname=="  ":
            print("hello for fname ")
            return render_template('signup.html',error='enter correct name in last name  field  it can not be blank space only')
        if lname.isalpha() or lname.count(" ")==2 or lname.count(" ")==1:
            print(" correct input should continue")
        else:
            return render_template('signup.html',error='enter correct name in the name field it should be alphabet')
        if len(fname) >=20:
            return render_template('signup.html',error='name field can handel upto 20 character')

        # merging firstname and last name 
        name1=fname+" "+lname
        # print(f"kkkkkkkkkkkkkk{name1}KKKKKKKKKKK")
        # print(name1.isalpha())
        # if name1.isalpha():
        #     print(name1.isalpha())
        # else:
        #     return render_template('signup.html',error='enter correct name in the name field')
    
        if name1=="" or name1==" " or name1=="  ":
            print("hello nullll")
            return render_template('signup.html',error='enter correct name in the name field')
        
        gen1 = request.form['gender']
        phno = request.form['pno']
        adhar = request.form['adhar']
        dob = request.form['birthday']
        email1 = request.form['email']
        pin = request.form['pincode']

        l.append(f'{pat_id} ')
        l.append(f'{name1} ')
        l.append(f'{email1}')
        l.append(f'{gen1}')
    

    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    # cursor.execute('SELECT * FROM accounts WHERE username = % s', (username, ))
    # account = cursor.fetchone()

# mysql> desc pat_info;
# +------------+--------------+------+-----+---------+-------+
# | Field      | Type         | Null | Key | Default | Extra |
# +------------+--------------+------+-----+---------+-------+
# | id         | varchar(14)  | NO   | PRI | NULL    |       |
# | fname      | varchar(50)  | NO   |     | NULL    |       |
# | lname      | varchar(50)  | NO   |     | NULL    |       |
# | email      | varchar(100) | NO   |     | NULL    |       |
# | gender     | varchar(100) | NO   |     | NULL    |       |
# | dob        | varchar(100) | NO   |     | NULL    |       |
# | adhar      | varchar(100) | NO   |     | NULL    |       |
# | phno       | varchar(100) | NO   |     | NULL    |       |
# | postalcode | varchar(100) | NO   |     | NULL    |       |
# | score      | varchar(100) | NO   |     | NULL    |       |
# | result     | varchar(100) | NO   |     | NULL    |       |
# +------------+--------------+------+-----+---------+-------+
# 11 rows in set (0.00 sec)

    cursor.execute('INSERT INTO pat_info VALUES (% s, % s, % s, % s, % s, % s, % s, % s, % s,% s,% s)',
                   (pat_id,fname,lname, email1, gen1, dob, adhar, phno, pin, sc, res ))
    mysql.connection.commit()
    msg = 'You have successfully registered !'
# calling a normal pyhton function to store the  fetching email value (from the form that is created in the signup page) and in that funcion we assign to a global variable email
    # function for context processor so that it can be avialable in all the template html
    making_global_info(name1, email1, pin, gen1, dob,pat_id)
    # makining the email as global variable so that we can able to use it in all the Function
    makeadharglob(adhar)
    return render_template('table.html',id=gpid, nm=name1, gen=gen1, pin=pin, dob=dob, email=email1,msg=msg)






# @app.route('/success/<string:sco>')
# def success(sco):
#     res = ""
#     print(sco)
#     score=int(sco)
#     print(score)


    # if score >= 4:
    #     res = "NEED TO CHECHK UP"
    # else:
    #     res = "NO NEED TO CHECHK UP"

    # cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    # k=str(score)#convert store to string as it is varchar in the msql databse
    # cursor.execute('UPDATE pat_info SET score =% s,result =% s WHERE id =% s', (k, res, gpid,))
    # mysql.connection.commit()

    # return render_template('result.html', result=res, sc=score, id=gpid)


@app.route('/fail/<string:s>')
def fail(s):
    return s+"please enter the valid input as written in the webpage"




# after pressing the submit button in the index.html page  app.route(/submit ) is going to executed
@app.route('/submit', methods=['POST', 'GET'])
def submit():
    # declaring global Variable to use within the submit function
    score = 0
    # mail=email
    
    res=" "

    if request.method == 'POST':
        try:
            p1 = int(request.form.get('age'))
            p2 = int(request.form.get('2pp'))
            p3 = int(request.form.get('3pp'))
            p4 = int(request.form.get('4pp'))
            p5 = int(request.form.get('5pp'))
            p6 = int(request.form.get('6pp'))
            print(f"the value of 1pp{p1}")
            print(f"the value of 2pp{p2}")
            print(f"the value of 3pp{p3}")
            print(f"middle one")
            print(f"the value of 4pp{p4}")
            print(f"the value of 5pp{p5}")
            print(f"the value of 6pp{p6}")
        except:
            
            return render_template('table.html',error='enter the valid input',id=gpid, nm=pname, gen=pgender, pin=ppin, dob=pdob, email=pemail)
            # pemail, pdob, pgender, ppin, pname, gpid
            # id=gpid, nm=name1, gen=gen1, pin=pin, dob=dob, email=email1,msg=msg
     
        if (p1 > 3 or p1 < 0  ):
            return render_template('table.html',error='enter the valid input',id=gpid, nm=pname, gen=pgender, pin=ppin, dob=pdob, email=pemail)
          
        if (p2 > 2 or p2 < 0):
            return render_template('table.html',error='enter the valid input',id=gpid, nm=pname, gen=pgender, pin=ppin, dob=pdob, email=pemail)
        if (p3 > 1 or p3 < 0):

            return render_template('table.html',error='enter the valid input',id=gpid, nm=pname, gen=pgender, pin=ppin, dob=pdob, email=pemail)
        if (p4 > 3 or p4 < 0):
            return render_template('table.html',error='enter the valid input',id=gpid, nm=pname, gen=pgender, pin=ppin, dob=pdob, email=pemail)
        if (p5 > 2 or p5 < 0):
            return render_template('table.html',error='enter the valid input',id=gpid, nm=pname, gen=pgender, pin=ppin, dob=pdob, email=pemail)
        if (p6 > 2 or p6 < 0):
            return render_template('table.html',error='enter the valid input',id=gpid, nm=pname, gen=pgender, pin=ppin, dob=pdob, email=pemail)

        score = (p1+p2+p3+p4+p5+p6)
        print(score)
    print(f"the score after the loop is {score}")
    if score >= 4:
        res = "NEED TO CHECHK UP"
    else:
        res = "NO NEED TO CHECHK UP"

    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    k=str(score)#convert store to string as it is varchar in the msql databse
    cursor.execute('UPDATE pat_info SET score =% s,result =% s WHERE id =% s', (k, res, gpid,))
    mysql.connection.commit()

    return render_template('result.html', result=res, sc=score, id=gpid)


    # sendind the total score to success function
    # return redirect(url_for('success', sco=tc))
        

    

@app.route('/search', methods=['POST', 'GET'])
def search():
    if request.method == 'POST':
        drag_input=(request.form['primary_key']).lower()
        idata=(request.form['inp']).lower()
        print(drag_input)
        print(idata)
    
     
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        if drag_input =="patient id":
            if idata.isdigit():
                cursor.execute("SELECT * from pat_info WHERE id LIKE '%"+idata+"%' ; ")
                result=list(cursor.fetchall())
            else:
                return render_template('searchpage.html',error='enter the digit in the patient id ')
        elif drag_input =="last name":
            if idata.isalpha():
                cursor.execute("SELECT * from pat_info WHERE lname LIKE '%"+idata+"%'; ")
                result=list(cursor.fetchall())
            else:
                return render_template('searchpage.html',error='enter the alphabet in the lastname  ')
            
        elif drag_input =="first name":
            if idata.isalpha():
                cursor.execute("SELECT * from pat_info WHERE fname LIKE '%"+idata+"%'; ")
                result=list(cursor.fetchall())
            else:
                return render_template('searchpage.html',error='enter the alphabet in the first name ')
            
            
        else:
            return render_template('searchpage.html',error='enter valid inputs either in number or in alphabet special characterS ARE NOT ALLOWED')


        # cursor.execute('SELECT * from pat_info WHERE id LIKE %s or lname LIKE %s or fname LIKE  %s ',(pdata,pdata,pdata))
        # cursor.execute("SELECT * from pat_info WHERE id LIKE '%"+pdata+"' or lname LIKE '%"+pdata+"' or fname LIKE '%"+pdata+"'; ")
        # cursor.execute("SELECT * from pat_info WHERE id LIKE '"+idata+"%' or lname LIKE '"+idata+"%' or fname LIKE '"+idata+"%'; ")
        # result=list(cursor.fetchall())
        print(result)
        return render_template('searchpage.html',parent_list=result)


# display the all record of the employee after pressing the all data button

@app.route('/all_data', methods=['POST', 'GET'])
def all_data():
    if request.method == 'POST':
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM pat_info')
        result=list(cursor.fetchall())
        print(result)
        print(type(result))
        print(result[0]['id'])
        
        return render_template('searchpage.html',parent_list=result)


