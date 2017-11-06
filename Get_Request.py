import os
from flask import Flask, url_for, request

app = Flask(__name__)

@app.route('/login', methods = ['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        return "username is" + request.values["username"]
    else:
        return '<form method="post" action = "/login"><input type = "text" name ="username"><button type="submit">Submit</button></form>'
        

if __name__== '__main__':
    host = os.getenv('IP','0.0.0.0')
    port = int(os.getenv('PORT', 6000))
    app.debug = True
    app.run(host=host, port=port)