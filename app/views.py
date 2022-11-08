from app import app
# from app import models


from flask import render_template
from cgitb import html
from flask import Flask, redirect, url_for, render_template, request


from flask_mysqldb import MySQL





@app.route('/')
def index():
    return render_template('initial.html')

@app.route('/signuppage')
def signuppage():
    return render_template('signup.html')


@app.route('/searchpage',methods=['GET', 'POST'])
def searchpage():
    return render_template('searchpage.html')

@app.route('/link')
def link():
    return render_template('link.html')


@app.route('/feedback')
def feedback():
    return render_template('feedback.html')



# when we tap to the back button it will go to the index.html page
@app.route('/back', methods=['POST', 'GET'])
def back():
    if request.method == 'POST':
        return render_template('signup.html')


# for invalid url user goes 
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404
 


 
# internal server error 
@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'),500
 