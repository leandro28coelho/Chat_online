from flask import Flask, render_template, request
import sqlite3
import hashlib

app = Flask(__name__, static_url_path='/static/')


def bate_papo():
    conexao = sqlite3.connect("banco.db")
    conexao.row_factory = sqlite3.Row
    data = conexao.execute('SELECT * FROM Code ORDER BY ID DESC').fetchall()
    return data

# Direciona para pagina Login
@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return render_template('index.html')


    else:
        return render_template('index.html', nick='leandro')





if __name__ == '__main__':
    app.run()



'''
200 OK (OK)
201 Created (Criado)
204 No Content (Sem conteúdo)
400 Bad Request (Requisição inválida)
401 Unauthorized (Não autorizado)
403 Forbidden (Proibido)
404 Not Found (Não encontrado)
405 Method Not Allowed (Método não permitido)
409 Conflict (Conflito)
500 Internal Server Error (Erro interno do servidor)
502 Bad Gateway (Gateway ruim)
503 Service Unavailable (Serviço indisponível)
504 Gateway Timeout (Tempo limite do gateway)
'''