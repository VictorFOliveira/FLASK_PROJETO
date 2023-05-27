
from flask import Flask # A importação do Flask para utilizar o framework Flask
from database import db # Criação do database em outro arquivo para evitar importação circular
from flask_migrate import Migrate # O migrate irá migrar as tabelas para o banco de dados
from usuarios import bp_usuarios # Usuários onde estará as rotas



app = Flask(__name__)

conexao = 'sqlite:///meubanco.sqlite'

# Conexão com o SQLALCHEMY ao SQLITE

app.config['SECRET_KEY'] = 'minha-chave'
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACKMODIFICATIONS'] = False
db.init_app(app)

app.register_blueprint(bp_usuarios,url_prefix='/alunos')


migrate = Migrate(app, db)

@app.route('/')
def index():
    return 'Olá, adicione /alunos na barra de pesquisa para iniciar o cadastro!'

app.run(debug=True, port=8080)