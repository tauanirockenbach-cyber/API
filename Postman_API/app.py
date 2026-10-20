#desenvolver um back-end com API -
#postman - teste http -> verificar respostas a API
#1. OBJETIVO
#2. URLBASE
#3. ENDPOINTS
#4. RESURSOS DISPONIBILIZADOS

#VAMOS CRIAR UMA API:

"""
1. CONSULTAR
2. CRIAR
3. EDITAR
4. EXCLUIR
C.R.U.D
"""
#Dar um pip install flask
from flask import Flask, jsonify, request
app = Flask(__name__)
#APP -> REPRESENTA A APLICAÇÃO FLASK
#__NAME__ -> IDENTIFICA QUE O MODULO DA APLICAÇÃO ESTÁ SENDO EXECUTADO COMO PROGRAMA PRINCIPAL

livros =[
    {
        "id": 1,
        "titulo": "A empregada",
        "autor": "Kathleen Barber"
    },
    {
        "id": 2,
        "titulo": "A hipotese do amor",
        "autor": "Ali Hazelwood"
    },
    {
        "id": 3,
        "titulo": "A revolução dos bichos",
        "autor": "George Orwell"
    },
    {
        "id": 4,
        "titulo": "O morro dos ventos uivantes",
        "autor": "Emily Dickinson"
    },
    {
        "id": 5,
        "titulo": "É Assim que Acaba",
        "autor": "Colleen Hoover"
    },
    {
        "id": 6,
        "titulo": "Jogo de amor para dois",
        "autor": "Ali Hazelwood"
    },
    {
        "id": 7,
        "titulo": "É Assim que Começa",
        "autor": "Colleen Hoover"
    },
    {
        "id": 8,
        "titulo": "Verity",
        "autor": "Colleen Hoover"
    },
    {
        "id": 9,
        "titulo": "Todas as Suas Imperfeições",
        "autor": "Colleen Hoover"
    },
    {
        "id": 10,
        "titulo": "As Mil Partes do Meu Coração",
        "autor": "Colleen Hoover"
    }
    
]

#CONSULTAR LIVROS
#def obter_livros():
    #return jsonify(livros)

#CRIAR AS ROTAS /LIVROS
#a rota foi especificada, somente o metodo GET será aceito
@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)

#CRIAR AS RROTAS /LIVROS/ID
@app.route('/livros/<int:id>', methods=['GET'])
#<int:> -> indica tipo inteiro
def obter_livro_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)
        elif livro.get('id') != id:
            return jsonify({'message': 'Livro não encontrado'}), 404

#PUT -> PRIMEIRO, OS DADOS ENVIADOS PELO CLIENTE, serao obtidos 
@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro_por_id(id):
    #permite acessar os dados json enviados no corpo da requisição
    livro_alterado = request.get_json()
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])

#CRIAÇÃO DE UM NOVO LIVRO
@app.route('/livros', methods=['POST'])
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(livros)

#EXCLUIR UM LIVRO
@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            livros.pop(indice)
            return jsonify(livros)
        return jsonify({'message': 'Livro não encontrado'}), 404

#INICIALIZAÇÃO DO SERVIDOR LOCAL
app.run(
    port=5001, 
    host='localhost',
    debug=True)