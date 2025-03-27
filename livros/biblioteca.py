import sqlite3

def criar_banco_biblioteca():
    # Conecta ao banco de dados (cria se não existir)
    conn = sqlite3.connect('biblioteca.db')
    cursor = conn.cursor()
    
    # Exclui tabelas se já existirem para evitar erros
    cursor.execute("DROP TABLE IF EXISTS LivroAutor")
    cursor.execute("DROP TABLE IF EXISTS Livros")
    cursor.execute("DROP TABLE IF EXISTS Autores")
    
    # Cria a tabela 
    cursor.execute('''
    CREATE TABLE Livros (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        ano_publicacao INTEGER,
        genero TEXT,
        isbn TEXT UNIQUE
    )
    ''')
    
    # Cria a tabela Autores
    cursor.execute('''
    CREATE TABLE Autores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        nacionalidade TEXT,
        data_nascimento TEXT
    )
    ''')
    
    # Cria a tabela de relacionamento LivroAutor (N:N)
    cursor.execute('''
    CREATE TABLE LivroAutor (
        livro_id INTEGER,
        autor_id INTEGER,
        PRIMARY KEY (livro_id, autor_id),
        FOREIGN KEY (livro_id) REFERENCES Livros (id),
        FOREIGN KEY (autor_id) REFERENCES Autores (id)
    )
    ''')
    
    # Insere alguns dados de exemplo na tabela Livros
    livros = [
        ('Dom Casmurro', 1899, 'Romance', '9788535909555'),
        ('O Senhor dos Anéis', 1954, 'Fantasia', '9788533613379'),
        ('1984', 1949, 'Ficção Científica', '9788522106169'),
        ('Memórias Póstumas de Brás Cubas', 1881, 'Romance', '9788535910663'),
        ('Harry Potter e a Pedra Filosofal', 1997, 'Fantasia', '9788532511010')
    ]
    
    cursor.executemany('INSERT INTO Livros (titulo, ano_publicacao, genero, isbn) VALUES (?, ?, ?, ?)', livros)
    
    # Insere alguns dados de exemplo na tabela Autores
    autores = [
        ('Machado de Assis', 'Brasileiro', '1839-06-21'),
        ('J.R.R. Tolkien', 'Britânico', '1892-01-03'),
        ('George Orwell', 'Britânico', '1903-06-25'),
        ('J.K. Rowling', 'Britânica', '1965-07-31')
    ]
    
    cursor.executemany('INSERT INTO Autores (nome, nacionalidade, data_nascimento) VALUES (?, ?, ?)', autores)
    
    # Insere os relacionamentos na tabela LivroAutor
    relacoes = [
        (1, 1), 
        (2, 2),  
        (3, 3), 
        (4, 1),  
        (5, 4)  
    ]
    
    cursor.executemany('INSERT INTO LivroAutor (livro_id, autor_id) VALUES (?, ?)', relacoes)
    
    
    conn.commit()
    conn.close()
    
    print("Banco de dados da biblioteca criado com sucesso!")


def consultar_livros_autores():
    conn = sqlite3.connect('biblioteca.db')
    cursor = conn.cursor()
    
    
    cursor.execute('''
    SELECT L.titulo, L.ano_publicacao, A.nome
    FROM Livros L
    JOIN LivroAutor LA ON L.id = LA.livro_id
    JOIN Autores A ON A.id = LA.autor_id
    ORDER BY L.titulo
    ''')
    
    resultados = cursor.fetchall()
    
    print("\n=== Livros e seus Autores ===")
    for resultado in resultados:
        print(f"Livro: {resultado[0]} ({resultado[1]}) - Autor: {resultado[2]}")
    
    conn.close()


if __name__ == "__main__":
    criar_banco_biblioteca()
    consultar_livros_autores()