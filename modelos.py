from database import db

class UserAluno(db.Model):
    """
    Classe que representa a tabela 'alunos' no banco de dados.

    Atributos:
    - id: Identificador único do aluno (chave primária).
    - nome: Nome do aluno.
    - matricula: Matrícula do aluno.
    - av1: Nota da primeira avaliação do aluno.
    - av2: Nota da segunda avaliação do aluno.

    Métodos:
    - __init__(self, nome, matricula, av1, av2): Construtor da classe UserAluno. Inicializa os atributos da classe.
    - calcular_media(self): Calcula a média das notas av1 e av2 do aluno.
    - __repr__(self): Retorna uma representação em string do objeto UserAluno.
    """
    __tablename__ = 'alunos'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)
    matricula = db.Column(db.String(100), nullable=False)
    av1 = db.Column(db.Integer, nullable=False)
    av2 = db.Column(db.Integer, nullable=False)
    
    def __init__(self, nome, matricula, av1, av2):
        """
        Construtor da classe UserAluno.

        Parâmetros:
        - nome: Nome do aluno.
        - matricula: Matrícula do aluno.
        - av1: Nota da primeira avaliação do aluno.
        - av2: Nota da segunda avaliação do aluno.
        """
        self.nome = nome
        self.matricula = matricula
        self.av1 = av1
        self.av2 = av2

    def calcular_media(self):
        """
        Calcula a média das notas av1 e av2 do aluno.

        Retorna:
        - A média das notas av1 e av2 do aluno.
        """
        return (self.av1 + self.av2) / 2

    def __repr__(self):
        """
        Retorna uma representação em string do objeto UserAluno.

        Retorna:
        - Uma string representando o objeto UserAluno.
        """
        return f'Usuario: {self.nome}'