from flask import Flask ,jsonify,request
import json

app = Flask(__name__)

tarefas = [
    {
        'id': 0,
        'responsavel': 'Bruno',
        'Tarefa': 'Refinamendo de demanda',
        'Status': 'Em analise'
    },
    {
        'id': 1,
        'responsavel':'Anderson',
        'Tarefa': 'Monitoramento Barramento',
        'Status': 'Executando'
    },
    {
        'id':2,
        'responsavel':'Thiago',
        'Tarefa': 'Desenvolver',
        'Status': 'Refinando o codigo'
    }
]
@app.route('/taf/<int:id>/', methods = ['PUT','GET'])
def execucao(id):
    if request.method == 'GET':
        execucao = tarefas[id]
        print(execucao)
        return jsonify(execucao)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        tarefas[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        execucao.pop(id)
        return  jsonify({'Status': 'sucesso', 'mensagem':'Registro deletado'})


if __name__ == '__main__':
    app.run(debug=True)
