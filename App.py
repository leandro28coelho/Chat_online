from flask import Flask, render_template, request
import sqlite3
import hashlib
VALOR='Anonymous'
app = Flask(__name__, static_url_path='/static/')


def limpeza():
    # verifica a quantidade de registro no banco de dados, quando atingir 50 registros o banco é limpo
    conexao = sqlite3.connect("banco.db")
    cursor = conexao.cursor()
    total = cursor.execute('SELECT COUNT(*) FROM Chat').fetchone()[0]
    if total > 50:
        cursor.execute('DELETE FROM Chat')
        conexao.commit()
        conexao.close()

    else:
        pass

# mostra as conversas salva do banco de dados.
def historico():
    conexao = sqlite3.connect("banco.db")
    conexao.row_factory = sqlite3.Row
    data = conexao.execute('SELECT * FROM Chat ORDER BY ID ASC').fetchall()
    limpeza()
    return data


# cria o banco de dados e salva as conversas.
def bate_papo(nome, texto):
    conexao = sqlite3.connect("banco.db")  # Banco de Dados
    curso = conexao.cursor()

    curso.execute('''
                    CREATE TABLE IF NOT EXISTS Chat (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT, 
                    NOME TEXT, 
                    TEXTO TEXT
                    )''')
    conexao.commit()

    try:
        curso.execute("INSERT INTO Chat (NOME, TEXTO) VALUES (?, ?)",
                      (str(nome), str(texto)))
        conexao.commit()
        conexao.close()

    except:
        print('Erro ao salvar chat')


@app.route('/mensagem', methods=['GET'])
def mensagem():
    print('rodou')
    return render_template('mensagem.html', registros=historico())



@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET', 'POST'])
@app.route('/chat', methods=['GET', 'POST'])
def chat():
    global VALOR
    # recebe o nome e o texto para salvar no banco de dados
    if request.method == 'POST':
        texto = request.form['texto']
        if texto == '':
            return render_template('chat.html', registros=historico())

        else:
            bate_papo(VALOR, texto)
            return render_template('chat.html', registros=historico())


    # solicitação GET
    else:
        return render_template('chat.html', registros=historico())


def limpar():
    conexao = sqlite3.connect("banco.db")
    cursor = conexao.cursor()
    cursor.execute('DELETE FROM Chat')
    conexao.commit()
    conexao.close()


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
