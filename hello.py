import json
from datetime import date

from flask import Flask, request

app = Flask(__name__)

user_bd = [
]

@app.route("/cadastronovo", methods=['POST'])
def hello_world():

    user = request.json
    user['data_de_criacao'] = str(date.today())
    user['data_ultima_atualiazacao'] = str(date.today()) 
    user['ultimo_login'] = " "
    user['data_de_criacao'] = str(date.today())
    user['token'] = " "
    user['id'] = len(user_bd) + 1
    for usuario in user_bd:
        if usuario['email'] == user["email"]:
            return "Esse email ja existe!", 409
        
    if len(user['phones']['number']) != 9:
        return 'Telefone invalido!', 400


    user_bd.append(request.json)
    return json.dumps(user_bd)

@app.route("/login", methods=['POST'])
def holla_mundo():
    user = request.json

    for usuario in user_bd:
        if usuario['email'] == user['email'] and \
           usuario['password'] == user ['password']:
            return user
            

    return 'usuario nao encontrado', 404




