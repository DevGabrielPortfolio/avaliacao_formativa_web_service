from flask import Flask, render_template, request, redirect, url_for
from model.control_messages import Mensagem

app = Flask(__name__)


@app.route('/')
def paginaInicial():
    return render_template('index.html')

@app.route('/ver_requisitos')
def page_requirements():
    requisitos = Mensagem.recuperar_requisitos()
    return render_template('requisitos.html', requisitos=requisitos)

@app.route('/post/cadastrar_requisitos', methods = ["POST"])
def post_message():
    descricao = request.form['descricao']
    nivel = request.form['nivel']
    valor = request.form['valor']

    Mensagem.cadastrar_requisito(descricao, nivel, valor)

    return redirect('/ver_requisitos')

@app.route('/deleteRequisito/<codigo>')
def deleteRequisito(codigo):
    Mensagem.delete_requisito(codigo)
    return redirect('/ver_requisitos')

@app.route('/marcarRequisito/resolvido/<codigo>')
def requisitoResolvido(codigo):
    Mensagem.update_requisito(codigo, 'Resolvido')
    return redirect('/ver_requisitos')

@app.route('/marcarRequisito/pendente/<codigo>')
def requisitoPendente(codigo):
    Mensagem.update_requisito(codigo, 'Pendente')
    return redirect('/ver_requisitos')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)