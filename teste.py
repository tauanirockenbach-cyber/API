#Uma API é um jeito de conectar sistemas, interface de programação de aplicações;
#API é um conjunto de regras e padrões que permite que diferentes sistemas de softwares se comuniquem e troquem dados entre si.

#Neste exemplo, será utilizada a *WEATHERapi.com* para consultar as condições climáticas de uma determinada localidade.

#consumir API ->
#Vamos precisar de um programa que tenha uma certa capacidade de pegar dados mediante a uma url pré definida
#vamos precisar da API key -> uma credencial

import requests #biblioteca para fazer requisições HTTP
from pprint import pprint #biblioteca para imprimir o dados de forma mais legível

API_key = "sua chave"
API_link = "seu link" 
cidade = str(input("Digite o nome do lugar: "))
linguagem = str(input("Digite a linguagem desejada: "))
print("\n")

parametros ={ 
    "key":API_key,
    "q":cidade, #cidade para qual queremos obter os dados
    "lang":linguagem, #linguagem
    "wind100kph": "true"
}
#armazenando a resposta da requisição na variavel resposta 

resposta = requests.get(API_link, params=parametros)
print(resposta.status_code) #status code: 200 (sucesso) ou 401 (erro)
print(resposta.content)
print("\n")
if resposta.status_code == 200:
    print("\033[32mRequisição realizada com sucesso!\033[0m")
    print("\n")
    dados = resposta.json() #arrmazenando os dados em formato JSON na variavel dados
    #pprint(dados) #.json() para deixar organizado
    temperatura = dados["current"]["temp_c"] #armazenando a temp em °C
    descricao = dados["current"]["condition"]["text"] #armazenando a descrição 
    vento = dados["current"]["wind_kph"] #armazenando a velocidade do vento
    print("\033[33mDADOS CLIMÁTICOS\033[0m")
    print(f"A temperatura atual do local escolhido é de {temperatura} °C")
    print(f"Descrição do clima: {descricao}")
    print(f"A velocidade do vento é de {vento} km/h")
    print("\n")

else:
    print("Erro na requisição.")



     