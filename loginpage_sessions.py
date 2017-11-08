import os
from flask import Flask, url_for, request, render_template, redirect, flash, session
import logging
from logging.handlers import RotatingFileHandler
import pymysql



app = Flask(__name__)

@app.route('/login', methods = ['GET','POST'])
def login_page():
    error = None
    if request.method == 'POST':
        if valid_login(request.form["username"], request.form["password"]):
            flash("Successfully logged in")
            session['username'] = request.form.get('username')
            return redirect(url_for('welcome'))
        
        else:
            error = "Enter username and password"
            app.logger.warning("incorrect username or password for",request.form.get('username'))
    return render_template('login.html', error = error)
        
@app.route('/logout')
def logout():
    session.pop('username',None)
    return redirect(url_for('login_page'))
       
def valid_login(username, password):
    
    MYSQL_DATABASE_HOST = os.getenv('IP','0.0.0.0')
    MYSQL_DATABASE_USER = 'vtripat3'
    MYSQL_DATABASE_PASSWORD = ''
    MYSQL_DATABASE_DB = 'myflask_appdb'
    connection = pymysql.connect(host = MYSQL_DATABASE_HOST, user = MYSQL_DATABASE_USER, password = MYSQL_DATABASE_PASSWORD, db = MYSQL_DATABASE_DB)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM user WHERE username ='%s' AND password = '%s'" %(username,password))
    data = cursor.fetchone()
    
    if data:
        return True
    else:
        return False
        
@app.route('/')
def welcome():
    if 'username' in  session:
        return render_template('welcome.html',username_template = session['username'])
    else:
        return redirect(url_for('login_page'))
            

if __name__== '__main__':
    host = os.getenv('IP','0.0.0.0')
    port = int(os.getenv('PORT', 8000))
    app.debug = True
    app.secret_key = 'Supersecretkey'
    handler = RotatingFileHandler('error.log',maxBytes = 10000, backupCount = 1)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    app.run(host=host, port=port)