import os
from flask import Flask, url_for

app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return 'Hello, World'
    
@app.route('/')
def indexPage():
    return url_for('printUserName', username="vibhuti")
    
@app.route('/user/<username>')
def printUserName(username):
    return "Hello user " + username
    
@app.route('/post/<int:postID>')
def postMethod(postID):
    return "post ID is " + str(postID)


if __name__== '__main__':
    host = os.getenv('IP','0.0.0.0')
    port = int(os.getenv('PORT', 5000))
    app.debug = True
    app.run(host=host, port=port)