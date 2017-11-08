import os
from flask import Flask, url_for, request, render_template, redirect, flash, make_response

app = Flask(__name__)

@app.route('/login', methods = ['GET','POST'])
def login_page():
    error = None
    if request.method == 'POST':
        if valid_login(request.form["username"], request.form["password"]):
            flash("Successfully logged in")
            #return redirect(url_for('method_redirect', username = request.form.get('username')))
            response = make_response(redirect(url_for('method_redirect')))
            response.set_cookie('username', request.form.get('username'))
            return response
        else:
            return "Do Not Match"
    else:
        error = "Enter username and password"
        return render_template('login.html', error = error)
        
@app.route('/logout')
def logout():
    response = make_response(url_for('login_page'))
    response.set_cookie('username','', expires = 0)
    return response
       
def valid_login(username, password):
    if username == password:
        return True
    else:
        return False
        
@app.route('/')
def method_redirect():
    username = request.cookies.get('username')
    if username:
        return render_template('welcome.html',username_template = username)
    else:
        return redirect(url_for('login_page'))
            

if __name__== '__main__':
    host = os.getenv('IP','0.0.0.0')
    port = int(os.getenv('PORT', 6000))
    app.debug = True
    app.secret_key = 'Supersecretkey'
    app.run(host=host, port=port)