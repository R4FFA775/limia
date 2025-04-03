import banco
import datetime

def menu():
    """Exibe o menu principal."""
    print("\n=== Sistema Bancário ===")
    print("1. Criar Conta")
    print("2. Consultar Saldo")
    print("3. Depositar")
    print("4. Sacar")
    print("5. Transferir")
    print("6. Extrato")
    print("7. Sair")
    return input("Escolha uma opção: ")

def criar_conta(conexao):
    nome = input("Digite o nome do cliente: ")
    cpf = input("Digite o CPF do cliente: ")
    conta_id = banco.criar_conta(conexao, nome, cpf)
    if conta_id:
        print(f"Conta criada com sucesso! ID da conta: {conta_id}")
    else:
        print("Erro ao criar conta.")

def consultar_saldo(conexao):
    conta_id = int(input("Digite o ID da conta: "))
    conta = banco.obter_conta(conexao, conta_id)
    if conta:
        print(f"Saldo da conta {conta_id}: R$ {conta[3]:.2f}")
    else:
        print("Conta não encontrada.")

def depositar(conexao):
    conta_id = int(input("Digite o ID da conta: "))
    valor = float(input("Digite o valor a depositar: "))
    conta = banco.obter_conta(conexao, conta_id)
    if conta:
        novo_saldo = conta[3] + valor
        banco.atualizar_saldo(conexao, conta_id, novo_saldo)
        data = datetime.datetime.now().isoformat()
        banco.registrar_transacao(conexao, conta_id, 'deposito', valor, data)
        print("Depósito realizado com sucesso.")
    else:
        print("Conta não encontrada.")

def sacar(conexao):
    conta_id = int(input("Digite o ID da conta: "))
    valor = float(input("Digite o valor a sacar: "))
    conta = banco.obter_conta(conexao, conta_id)
    if conta:
        if conta[3] >= valor:
            novo_saldo = conta[3] - valor
            banco.atualizar_saldo(conexao, conta_id, novo_saldo)
            data = datetime.datetime.now().isoformat()
            banco.registrar_transacao(conexao, conta_id, 'saque', valor, data)
            print("Saque realizado com sucesso.")
        else:
            print("Saldo insuficiente.")
    else:
        print("Conta não encontrada.")

def transferir(conexao):
    conta_origem_id = int(input("Digite o ID da conta de origem: "))
    conta_destino_id = int(input("Digite o ID da conta de destino: "))
    valor = float(input("Digite o valor a transferir: "))

    conta_origem = banco.obter_conta(conexao, conta_origem_id)
    conta_destino = banco.obter_conta(conexao, conta_destino_id)

    if conta_origem and conta_destino:
        if conta_origem[3] >= valor:
            novo_saldo_origem = conta_origem[3] - valor
            novo_saldo_destino = conta_destino[3] + valor

            banco.atualizar_saldo(conexao, conta_origem_id, novo_saldo_origem)
            banco.atualizar_saldo(conexao, conta_destino_id, novo_saldo_destino)

            data = datetime.datetime.now().isoformat()
            banco.registrar_transacao(conexao, conta_origem_id, 'transferencia', -valor, data)  # Saída
            banco.registrar_transacao(conexao, conta_destino_id, 'transferencia', valor, data)   # Entrada

            print("Transferência realizada com sucesso.")
        else:
            print("Saldo insuficiente na conta de origem.")
    else:
        print("Uma ou ambas as contas não foram encontradas.")

def exibir_extrato(conexao):
    conta_id = int(input("Digite o ID da conta: "))
    conta = banco.obter_conta(conexao, conta_id)
    if conta:
        transacoes = banco.obter_transacoes(conexao, conta_id)
        print(f"\n=== Extrato da Conta {conta_id} ===")
        for transacao in transacoes:
            print(f"Tipo: {transacao[2]}, Valor: R$ {transacao[3]:.2f}, Data: {transacao[4]}")
        print(f"Saldo atual: R$ {conta[3]:.2f}")
    else:
        print("Conta não encontrada.")

def main():
    conexao = banco.criar_conexao()
    if conexao:
        banco.criar_tabelas(conexao)

        while True:
            opcao = menu()

            if opcao == '1':
                criar_conta(conexao)
            elif opcao == '2':
                consultar_saldo(conexao)
            elif opcao == '3':
                depositar(conexao)
            elif opcao == '4':
                sacar(conexao)
            elif opcao == '5':
                transferir(conexao)
            elif opcao == '6':
                exibir_extrato(conexao)
            elif opcao == '7':
                print("Saindo do sistema bancário...")
                break
            else:
                print("inválida.")

        conexao.close()

if __name__ == "__main__":
    main()