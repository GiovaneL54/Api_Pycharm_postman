from idlelib.mainmenu import menudefs

from flask import Flask, jsonify, request  # explicação esta no App
import json

app = Flask(__name__)
#Criando uma lista
desenvolvedores = [
    {
     'ID': 0,
     'Nome':'Giovane',
     'Habilidades:':['Python','Dormir','Colocar os outros acima dele mesmo']  #criando uma lista em json
    },
    {
     'ID': 1,
     'Nome':'Rafael',
     'Habilidades:':['Python','Flask']
     },

]

# devolve um desenvolvedor por id , tambem altera e deleta um desenvolvedor
@app.route('/dev/<int:id>/', methods = ['POST','GET','DELETE','PUT']) #int entra como um paramentro para poder definir como inteiro (GET recupera e PUT altera)
def desenvolvedor(id):
    #para distinguir de get ou put vamos usar o if
    if request.method == 'GET':  #Neste caso o GET vai retornar essas informações abaixo
        desenvolvedor = desenvolvedores[id] #atribuindo o construtor a variavel que recebe a lista.
        print(desenvolvedor)
        return jsonify(desenvolvedor)

    #melhorando o GET:
    elif request.method == 'GET':  #Neste caso o GET vai retornar essas informações abaixo apos usar o DELETE:
        try:
            response = desenvolvedores[id] #atribuindo o construtor a variavel que recebe a lista.
        except IndexError:
            mensagem = 'Desenvolvedor de ID {} nao existe'.format(id)
            response = {'Status': 'erro','mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o administrador da API'
            response = {'Status': 'Erro', 'mensagem': mensagem}
        return jsonify(response)


    elif request.method == 'PUT': #para alterar
        dados = json.loads(request.data) #atribuindo a variavel para receber os dados da variavel desenvolvedor
        desenvolvedores[id] = dados
        #pass  ira passar caso esse metodo seja chamado
        return jsonify(dados)
        #No caso para alterar sera feito no postman selecione o caminho: PUT - clique em body / raw / na mesma linha do raw selecione json
    #Usando o DELETE
    elif request.method == 'DELETE':
        desenvolvedores.pop(id) #Comando para deletar
        return jsonify({'Status': 'sucesso', 'mensagem':'Registro excluido'})
        #voce abre o postman e coloca a url e seleciona o dele no canto esquerdo e clica em enviar (coloque a url completa e o id) caso de certo ele retornara a
        #mensagem que voce colocou no jsonify apos deletar caso voce consulte no GET ira retonar erro 500 pois nao achou o cadastro.


#lista todos os desenvolvedores e tambem permite registrar um novo desenvolvedor
@app.route('/dev/', methods = ['POST','GET',])
def lista_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        #Demonstrando os id dos desenvolvedores
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        #return jsonify({'status':'sucesso', 'menssagem': 'Registro inserido'})
        #para retornar os desenvolvedores na posicao
        return jsonify(desenvolvedores[posicao])
    #consultando todos os desenvolvedores:
    elif request.method == 'GET':
        return jsonify(desenvolvedores)


if __name__ == '__main__':
    app.run(debug=True) #O run executa o app e o debug atualiza conforme codigo vai sendo atualizado
#AO executar sera fornecido um ip para colocar no navegador. insira o /dev/id na frente (id coloque um numero para exibir o resultado.