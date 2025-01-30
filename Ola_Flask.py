from functools import total_ordering

from flask import Flask #importando a biblioteca
import json
app = Flask(__name__)

@app.route("/") #depurador e a rota para o Flask
def ola(): #função
    return 'Ola mundo'
#--------------------
#Para ultiliza no postman e sera necessario a mudança nessa parte do codigo:
# @app.route("/")  deve ficar assim: @app.route("/", methods=['GET','POST'])
# apos fazer essa modificação nao funcionara no navegador. tera que colocar esse ip de acesso no campo de pesquisa.
#Apos colocar esse codigo no campo voce deve altera para POST ou GET e pesquisar para porder executar nesse exempo funciona no navegador tambem devido o GET

#Executando com numero:
#@app.route("/<numero>") #depurador e a rota para o Flask usando numero. Deve inserir um numero como parametro depois do ip para ter o retorno.
#def ola(numero): #função
#    return 'Ola mundo. {}'.format(numero)

@app.route('/soma',methods=['POST', 'GET']) #Com o metodos post e possivel passar valores.
def soma():
    if request.method == 'POST':
        dados = json.loads(request.data)
        total = sum(dados['valores'])
    elif request.method == 'GET':
        total = 10 + 10
    return jsonify({'soma':total})

if __name__=="__main__":  #Com essa função if somente sera executado se esse codigo chamar o app.
    app.run(debug=True) #Executor. No modo debug ao efetuar uma alteração ele reistarta sozinho.
#ao executar o terminal ira informar um endereço link com endereço de ip http://127.0.0.1:5000
#ao colocar ele no navegador a pagina ira retornar o que setado no return.