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
def criar_tabela_produtos(conexao):
    """Cria a tabela de produtos no banco de dados"""
    try:
        cursor = conexao.cursor()
        cursor.execute('DROP TABLE IF EXISTS produtos')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS produtos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                preco REAL NOT NULL,
                quantidade INTEGER NOT NULL
            )
        ''')
        conexao.commit()
        print("Tabela produtos criada com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao criar tabela de produtos: {e}")

def cadastrar_produto(conexao):
    """Cadastra um novo produto no banco de dados"""
    try:
        nome = input("Nome do produto: ")
        preco = float(input("Preço do produto: "))
        quantidade = int(input("Quantidade do produto: "))
        
        cursor = conexao.cursor()
        cursor.execute('''
            INSERT INTO produtos (nome, preco, quantidade)
            VALUES (?, ?, ?)
        ''', (nome, preco, quantidade))
        conexao.commit()
        print("Produto cadastrado com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao cadastrar produto: {e}")
    except ValueError:
        print("Valor inválido. Tente novamente.")
    except Exception as e:
        print(f"Erro inesperado: {e}")

def listar_produtos(conexao):
    """Lista todos os produtos cadastrados no banco de dados"""
    try:
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM produtos')
        produtos = cursor.fetchall()
        
        if produtos:
            print("Produtos cadastrados:")
            for produto in produtos:
                print(f"ID: {produto[0]}, Nome: {produto[1]}, Preço: {produto[2]}, Quantidade: {produto[3]}")
        else:
            print("Nenhum produto cadastrado.")
    except sqlite3.Error as e:
        print(f"Erro ao listar produtos: {e}")

def criar_tabela_clientes(conexao):
    """Cria a tabela de clientes no banco de dados"""
    try:
        cursor = conexao.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                cpf TEXT NOT NULL UNIQUE
            )
        ''')
        conexao.commit()
    except sqlite3.Error as e:
        print(f"Erro ao criar tabela de clientes: {e}")
def cadastrar_cliente(conexao):
    """Cadastra um novo cliente no banco de dados"""
    try:
        nome = input("Nome do cliente: ")
        cpf = input("CPF do cliente: ")
        
        cursor = conexao.cursor()
        cursor.execute('''
            INSERT INTO clientes (nome, cpf)
            VALUES (?, ?)
        ''', (nome, cpf))
        conexao.commit()
        print("Cliente cadastrado com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao cadastrar cliente: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")
def listar_clientes(conexao):   
    """Lista todos os clientes cadastrados no banco de dados"""
    try:
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM clientes')
        clientes = cursor.fetchall()
        
        if clientes:
            print("Clientes cadastrados:")
            for cliente in clientes:
                print(f"ID: {cliente[0]}, Nome: {cliente[1]}, CPF: {cliente[2]}")
        else:
            print("Nenhum cliente cadastrado.")
    except sqlite3.Error as e:
        print(f"Erro ao listar clientes: {e}")

def tabelas_pedidos(conexao):
    """Cria a tabela de pedidos no banco de dados"""
    try:
        cursor = conexao.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS pedidos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                cliente_id INTEGER NOT NULL,
                produto_id INTEGER NOT NULL,
                quantidade INTEGER NOT NULL,
                data TEXT NOT NULL,
                FOREIGN KEY (cliente_id) REFERENCES clientes (id),
                FOREIGN KEY (produto_id) REFERENCES produtos (id)
            )
        ''')
        conexao.commit()
    except sqlite3.Error as e:
        print(f"Erro ao criar tabela de pedidos: {e}")
def cadastrar_pedido(conexao):
    """Cadastra um novo pedido no banco de dados"""
    try:
        cliente_id = int(input("ID do cliente: "))
        produto_id = int(input("ID do produto: "))
        quantidade = int(input("Quantidade do produto: "))
        data = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        cursor = conexao.cursor()
        cursor.execute('''
            INSERT INTO pedidos (cliente_id, produto_id, quantidade, data)
            VALUES (?, ?, ?, ?)
        ''', (cliente_id, produto_id, quantidade, data))
        conexao.commit()
        print("Pedido cadastrado com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao cadastrar pedido: {e}")
    except ValueError:
        print("Valor inválido. Tente novamente.")
    except Exception as e:
        print(f"Erro inesperado: {e}")
def listar_pedidos(conexao):
    """Lista todos os pedidos cadastrados no banco de dados"""
    try:
        cursor = conexao.cursor()
        cursor.execute('''
            SELECT pedidos.id, clientes.nome, produtos.nome, pedidos.quantidade, pedidos.data
            FROM pedidos
            JOIN clientes ON pedidos.cliente_id = clientes.id
            JOIN produtos ON pedidos.produto_id = produtos.id
        ''')
        pedidos = cursor.fetchall()
        
        if pedidos:
            print("Pedidos cadastrados:")
            for pedido in pedidos:
                print(f"ID: {pedido[0]}, Cliente: {pedido[1]}, Produto: {pedido[2]}, Quantidade: {pedido[3]}, Data: {pedido[4]}")
        else:
            print("Nenhum pedido cadastrado.")
    except sqlite3.Error as e:
        print(f"Erro ao listar pedidos: {e}")
def main():
    """Função principal do programa"""
    conexao = criar_conexao()
    if conexao is None:
        return
    
    criar_tabela_produtos(conexao)
    criar_tabela_clientes(conexao)
    tabelas_pedidos(conexao)
    
    while True:
        print("\nMenu:")
        print("1. Cadastrar produto")
        print("2. Listar produtos")
        print("3. Cadastrar cliente")
        print("4. Listar clientes")
        print("5. Cadastrar pedido")
        print("6. Listar pedidos")
        print("7. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            cadastrar_produto(conexao)
        elif opcao == '2':
            listar_produtos(conexao)
        elif opcao == '3':
            cadastrar_cliente(conexao)
        elif opcao == '4':
            listar_clientes(conexao)
        elif opcao == '5':
            cadastrar_pedido(conexao)
        elif opcao == '6':
            listar_pedidos(conexao)
        elif opcao == '7':
            break
        else:
            print("Opção inválida. Tente novamente.")
    
    conexao.close()
if __name__ == "__main__":
    main()