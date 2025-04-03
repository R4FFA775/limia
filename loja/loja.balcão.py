import sqlite3
import datetime

def criar_conexao():
    """Cria uma conexão com o banco de dados SQLite"""
    try:
        conexao = sqlite3.connect('loja.db')
        return conexao
    except sqlite3.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None
    
def menu():
    """Exibe o menu principal"""
    print("1. Criar banco de dados")
    print("2. Inserir dados")
    print("3. Listar produtos")
    print("4. Vender produto")
    print("5. Sair")
    print("Escolha uma opção:")
    opcao = input()
    return opcao
   