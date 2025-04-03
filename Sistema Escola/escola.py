import sqlite3

def criar_banco_dados():
 	
    conexao = sqlite3.connect('escola.db')
    cursor = conexao.cursor()

 #tabela criar de alunos

    cursor.execute('''
    CREATE TABLE Alunos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        data_nascimento TEXT,
        cpf TEXT UNIQUE
    )
    ''')
    # criar tabela de cursos

    cursor.execute('''
    CREATE TABLE Cursos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        carga_horaria INTEGER
    )
    ''')

    # criar tabela de matriculas

    cursor.execute('''
    CREATE TABLE Matriculas (
        aluno_id INTEGER,
        curso_id INTEGER,
        data_matricula TEXT,
        PRIMARY KEY (aluno_id, curso_id),
        FOREIGN KEY (aluno_id) REFERENCES Alunos (id),
        FOREIGN KEY (curso_id) REFERENCES Cursos (id)
    )
    ''')
    print('Banco de dados criado com sucesso!')
    return conexao, cursor

def inserir_dados(conexao,curso):

    alunos = [  
        ('joao',  '1990-01-01', '11111111111'),
        ('maria', '1991-02-02', '22222222222'),
        ('jose',  '1992-03-03', '33333333333'),
        ('ana',   '1993-04-04', '44444444444')

    ]

    cursos = [
        ('Python Fundamentos', 40),
        ('Estatistica', 40),
        ('Machine Learning', 40),
        ('Deep Learning', 40)
    ]

    matriculas = [

        (1, 1, '2020-01-01'),
        (1, 2, '2020-01-01'),
        (2, 2, '2020-01-01'),
        (2, 3, '2020-01-01'),
        (3, 3, '2020-01-01'),
        (3, 4, '2020-01-01'),
        (4, 4, '2020-01-01')
    ]

    cursor = conexao.cursor()
    cursor.executemany('INSERT INTO Alunos (nome, data_nascimento, cpf) VALUES (?, ?, ?)', alunos)
    cursor.executemany('INSERT INTO Cursos (nome, carga_horaria) VALUES (?, ?)', cursos)
    cursor.executemany('INSERT INTO Matriculas (aluno_id, curso_id, data_matricula) VALUES (?, ?, ?)', matriculas)
    conexao.commit()
    print('Dados inseridos com sucesso!')
    return cursor

def consultar_dados(cursor):
    print("\nAlunos cadastrados:")
    cursor.execute("SELECT id, nome, data_nascimento, cpf FROM Alunos")
    for aluno in cursor.fetchall():
        print(f"ID: {aluno[0]}, Nome: {aluno[1]}, Data de Nascimento: {aluno[2]}, CPF: {aluno[3]}")
    
    print("\nCursos disponíveis:")
    cursor.execute("SELECT id, nome, carga_horaria FROM Cursos")
    for curso in cursor.fetchall():
        print(f"ID: {curso[0]}, Nome: {curso[1]}, Carga Horária: {curso[2]} horas")
    
    print("\nMatrículas realizadas:")
    cursor.execute("""
        SELECT a.nome, c.nome, m.data_matricula 
        FROM Matriculas m
        JOIN Alunos a ON m.aluno_id = a.id
        JOIN Cursos c ON m.curso_id = c.id
    """)
    for matricula in cursor.fetchall():
        print(f"Aluno: {matricula[0]}, Curso: {matricula[1]}, Data: {matricula[2]}")


def main():
    conexao, cursor = criar_banco_dados()
    
    cursor = inserir_dados(conexao, cursor)
    
    consultar_dados(cursor)

    conexao.close()
    print("\nConexão com o banco de dados fechada.")

if __name__ == "__main__":
    main()
