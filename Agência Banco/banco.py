import sqlite3

DATABASE_NAME = 'banco.db'

def criar_conexao():
    try:
        conexao = sqlite3.connect(DATABASE_NAME)
        return conexao
    except sqlite3.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

def criar_tabelas(conexao):
    cursor = conexao.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cpf TEXT UNIQUE NOT NULL,
            saldo REAL DEFAULT 0.0
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transacoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            conta_id INTEGER NOT NULL,
            tipo TEXT NOT NULL,  -- 'deposito', 'saque', 'transferencia'
            valor REAL NOT NULL,
            data TEXT NOT NULL,
            FOREIGN KEY (conta_id) REFERENCES contas(id)
        )
    ''')

    conexao.commit()

def criar_conta(conexao, nome, cpf):
    cursor = conexao.cursor()
    try:
        cursor.execute("INSERT INTO contas (nome, cpf) VALUES (?, ?)", (nome, cpf))
        conexao.commit()
        return cursor.lastrowid 
    except sqlite3.IntegrityError:
        print("CPF já cadastrado.")
        return None

def obter_conta(conexao, conta_id):
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM contas WHERE id = ?", (conta_id,))
    return cursor.fetchone()

def atualizar_saldo(conexao, conta_id, novo_saldo):
    cursor = conexao.cursor()
    cursor.execute("UPDATE contas SET saldo = ? WHERE id = ?", (novo_saldo, conta_id))
    conexao.commit()

def registrar_transacao(conexao, conta_id, tipo, valor, data):
    cursor = conexao.cursor()
    cursor.execute('''
        INSERT INTO transacoes (conta_id, tipo, valor, data)
        VALUES (?, ?, ?, ?)
    ''', (conta_id, tipo, valor, data))
    conexao.commit()

def obter_transacoes(conexao, conta_id):
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM transacoes WHERE conta_id = ? ORDER BY data DESC", (conta_id,))
    return cursor.fetchall()