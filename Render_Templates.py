import os
from flask import Flask, url_for, request, render_template

app = Flask(__name__)

@app.route('/hello')
@app.route('/hello/<name>')
def hellomethod(name = None):
    return render_template('hello.html', name_template = name)

if __name__== '__main__':
    host = os.getenv('IP','0.0.0.0')
    port = int(os.getenv('PORT', 6000))
    app.debug = True
    app.run(host=host, port=port)