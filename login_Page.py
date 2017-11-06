import os
from flask import Flask, url_for, request, render_template, redirect, flash

app = Flask(__name__)

@app.route('/login', methods = ['GET','POST'])
def login_page():
    error = None
    if request.method == 'POST':
        if valid_login(request.form["username"], request.form["password"]):
            flash("Successfully logged in")
            return redirect(url_for('method_redirect', username = request.form.get('username')))
        else:
            return "Do Not Match"
    else:
        error = "Enter username and password"
        return render_template('login.html', error = error)
       
def valid_login(username, password):
    if username == password:
        return True
    else:
        return False
        
@app.route('/welcome/<username>')
def method_redirect(username):
    return render_template('welcome.html', username_template= username)
            

if __name__== '__main__':
    host = os.getenv('IP','0.0.0.0')
    port = int(os.getenv('PORT', 6000))
    app.debug = True
    app.secret_key = 'Supersecretkey'
    app.run(host=host, port=port)