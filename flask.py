from flask import Flask

env:FLASK_APP = "hello"

app = Flask(flask.py)



@app.route("localhost:5000/novousuario")
def hello_world():
    return "<p>Hello, World!</p>"
