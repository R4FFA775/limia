import sqlite3

import sqlite3

def criar_conexao():
    """Cria uma conexão com o banco de dados"""
    try:
        conexao = sqlite3.connect('meu_banco.db')
        print("Conexão com banco de dados criada com sucesso!")
        return conexao
    except sqlite3.Error as erro:
        print(f"Erro ao conectar ao banco de dados: {erro}")
        return None

def criar_tabela(conexao):
    """Cria uma tabela de exemplo"""
    try:
        cursor = conexao.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                idade INTEGER,
                email TEXT
            )
        ''')
        conexao.commit()
        print("Tabela criada com sucesso!")
    except sqlite3.Error as erro:
        print(f"Erro ao criar tabela: {erro}")

def inserir_usuario(conexao, nome, idade, email):
    """Insere um novo usuário na tabela"""
    try:
        cursor = conexao.cursor()
        cursor.execute('''
            INSERT INTO usuarios (nome, idade, email)
            VALUES (?, ?, ?)
        ''', (nome, idade, email))
        conexao.commit()
        print("Usuário inserido com sucesso!")
    except sqlite3.Error as erro:
        print(f"Erro ao inserir usuário: {erro}")

def main():
    # Criar conexão com o banco
    conexao = criar_conexao()
    if conexao is not None:
        # Criar tabela
        criar_tabela(conexao)
        
        # Inserir alguns dados de exemplo
        inserir_usuario(conexao, "Maria", 25, "maria@email.com")
        inserir_usuario(conexao, "João", 30, "joao@email.com")
        
        # Fechar conexão
        conexao.close()

if __name__ == "__main__":
    main()