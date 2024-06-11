from flask import Flask, request, jsonify
from gerenciador import Gerenciador
from seletor import Seletor
from validador import Validador
from utils import Utils

app = Flask(__name__)

gerenciador = Gerenciador()
seletor = Seletor()
validador = Validador()

# Rotas do Gerenciador
@app.route('/trans/create_account', methods=['POST'])
def create_account():
    data = request.json()
    validador.validar_create_account(data)
    gerenciador.criar_conta(data)
    return jsonify({'message': 'Conta criada com sucesso!'}), 201
