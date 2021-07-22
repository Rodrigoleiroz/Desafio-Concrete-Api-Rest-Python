from flask import Flask, request

app = Flask(__name__)
user_db = []

@app.route("/novousuario", methods=['POST'])
def cria_usuario():
    return request.json
user = request.json

 

app.run()

