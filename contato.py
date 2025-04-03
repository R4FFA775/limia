import sqlite3
from datetime import datetime

def criar_conexao():
    """Cria uma conexão com o banco de dados da agenda"""
    try:
        conexao = sqlite3.connect('agenda.db')
        return conexao
    except sqlite3.Error as erro:
        print(f"Erro ao conectar: {erro}")
        return None

def criar_tabela_contatos(conexao):
    """Cria a tabela de contatos"""
    try:
        cursor = conexao.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS contatos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                telefone TEXT NOT NULL,
                email TEXT,
                endereco TEXT,
                data_cadastro TEXT
            )
        ''')
        conexao.commit()
        print("Tabela de contatos criada com sucesso!")
    except sqlite3.Error as erro:
        print(f"Erro ao criar tabela: {erro}")

def adicionar_contato(conexao, nome, telefone, email="", endereco=""):
    """Adiciona um novo contato"""
    try:
        cursor = conexao.cursor()
        data_atual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute('''
            INSERT INTO contatos (nome, telefone, email, endereco, data_cadastro)
            VALUES (?, ?, ?, ?, ?)
        ''', (nome, telefone, email, endereco, data_atual))
        conexao.commit()
        print("Contato adicionado com sucesso!")
    except sqlite3.Error as erro:
        print(f"Erro ao adicionar contato: {erro}")

def listar_contatos(conexao):
    """Lista todos os contatos"""
    try:
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM contatos')
        contatos = cursor.fetchall()
        
        if not contatos:
            print("\nNenhum contato encontrado!")
            return

        print("\n=== Lista de Contatos ===")
        for contato in contatos:
            print(f"\nID: {contato[0]}")
            print(f"Nome: {contato[1]}")
            print(f"Telefone: {contato[2]}")
            print(f"Email: {contato[3] or 'Não informado'}")
            print(f"Endereço: {contato[4] or 'Não informado'}")
            print(f"Data de cadastro: {contato[5]}")
            print("-" * 30)
    except sqlite3.Error as erro:
        print(f"Erro ao listar contatos: {erro}")

def buscar_contato(conexao, termo):
    """Busca contatos por nome ou telefone"""
    try:
        cursor = conexao.cursor()
        cursor.execute('''
            SELECT * FROM contatos 
            WHERE nome LIKE ? OR telefone LIKE ?
        ''', (f'%{termo}%', f'%{termo}%'))
        contatos = cursor.fetchall()
        
        if not contatos:
            print("\nNenhum contato encontrado!")
            return

        print(f"\n=== Resultados da busca por '{termo}' ===")
        for contato in contatos:
            print(f"\nNome: {contato[1]}")
            print(f"Telefone: {contato[2]}")
            print("-" * 30)
    except sqlite3.Error as erro:
        print(f"Erro ao buscar contato: {erro}")

def menu():
    print("\n=== AGENDA DE CONTATOS ===")
    print("1. Adicionar contato")
    print("2. Listar todos os contatos")
    print("3. Buscar contato")
    print("4. Sair")
    return input("Escolha uma opção: ")

def main():
    conexao = criar_conexao()
    if conexao is None:
        return

    criar_tabela_contatos(conexao)
    
    while True:
        opcao = menu()
        
        if opcao == '1':
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            email = input("Email (opcional): ")
            endereco = input("Endereço (opcional): ")
            adicionar_contato(conexao, nome, telefone, email, endereco)
        
        elif opcao == '2':
            listar_contatos(conexao)
        
        elif opcao == '3':
            termo = input("Digite o nome ou telefone para buscar: ")
            buscar_contato(conexao, termo)
        
        elif opcao == '4':
            print("Encerrando agenda...")
            break
        
        else:
            print("Opção inválida!")

    conexao.close()

if __name__ == "__main__":
    main()