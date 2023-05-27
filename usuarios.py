from flask import Blueprint, render_template, request, redirect
from modelos import UserAluno
from database import db

# Criação de um Blueprint chamado 'alunos'
bp_usuarios = Blueprint('alunos', __name__, template_folder='templates')

@bp_usuarios.route('/', methods=['GET', 'POST'])
def criar_aluno():
    """
    Rota para criar um novo aluno no banco de dados.

    Se o método da requisição for POST, extrai os dados do formulário e cria um objeto aluno.
    Em seguida, adiciona o aluno ao banco de dados e redireciona para a rota de listagem de alunos.

    Caso contrário, renderiza o template 'criar_aluno.html'.
    """
    if request.method == 'POST':
        nome = request.form['nome']
        matricula = request.form['matricula']
        av1 = int(request.form['av1'])
        av2 = int(request.form['av2'])

        aluno = UserAluno(nome=nome, matricula=matricula, av1=av1, av2=av2)
        db.session.add(aluno)
        db.session.commit()
        return redirect('/alunos/listar')

    return render_template('criar_aluno.html')

@bp_usuarios.route('/listar')
def listar_alunos():
    """
    Rota para listar todos os alunos cadastrados no banco de dados.

    Recupera todos os registros da tabela UserAluno e renderiza o template 'lista_alunos.html'
    passando a lista de alunos como parâmetro para o template.
    """
    alunos = UserAluno.query.all()
    return render_template('lista_alunos.html', alunos=alunos)

@bp_usuarios.route('/atualizar/<int:id>', methods=['GET', 'POST'])
def atualizar_aluno(id):
    """
    Rota para atualizar os dados de um aluno existente no banco de dados.

    Recebe o ID do aluno como parâmetro na URL.
    Se o método da requisição for POST, atualiza os dados do aluno com base no formulário enviado.
    Em seguida, realiza o commit das alterações no banco de dados e redireciona para a rota de listagem de alunos.

    Caso contrário, renderiza o template 'alunos_update.html' passando o objeto aluno como parâmetro para o template.
    """
    aluno = UserAluno.query.get(id)

    if request.method == 'POST':
        aluno.nome = request.form['nome']
        aluno.matricula = request.form['matricula']
        aluno.av1 = float(request.form['av1'])
        aluno.av2 = float(request.form['av2'])

        db.session.commit()
        return redirect('/alunos/listar')
    
    else:
        request.method == 'GET'
        return render_template('alunos_update.html', aluno=aluno)

@bp_usuarios.route('/deletar/<int:id>', methods=['GET', 'POST'])
def deletar_aluno(id):
    """
    Rota para deletar um aluno do banco de dados.

    Recebe o ID do aluno como parâmetro na URL.
    Se o método da requisição for POST, deleta o aluno do banco de dados e realiza o commit das alterações.
    Em seguida, redireciona para a rota de listagem de alunos.

    Caso contrário, renderiza o template 'alunos_delete.html' passando o objeto aluno como parâmetro para o template.
    """
    aluno = UserAluno.query.get(id)

