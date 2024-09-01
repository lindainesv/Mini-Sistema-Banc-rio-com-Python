"""No Import"""

MENU = """
Digite a opção desejada:

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

SALDO = 0
LIMITE = 500
EXTRATO = ""
NUMERO_SAQUES = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(MENU)

    if opcao == "1":
        valor_deposito = float(input("Digite o valor de depósito: "))

        if valor_deposito > 0:
            SALDO += valor_deposito
            EXTRATO += f"Valor R$ {valor_deposito:.2f} depositado"

        else:
            print("Ocorreu um erro: valor invalido")

    elif opcao == "2":
        valor_saque = float(input("Informe o valor que deseja sacar: "))

        if valor_saque > SALDO:
            print("Saldo insuficiente.")

        elif valor_saque > LIMITE:
            print("Limite excedido.")

        elif NUMERO_SAQUES > LIMITE_SAQUES:
            print("Numero de saques excedido.")

        elif valor_saque > 0:
            SALDO -= valor_saque
            EXTRATO += f"\nValor R$ {valor_saque:.2f} sacado"
            NUMERO_SAQUES += 1

        else:
            print("Operação falhou. Valor informado inválido.")

    elif opcao == "3":
        print("\n========EXTRATO========")
        print("Sem movimentações na conta" if not EXTRATO else EXTRATO)
        print(f"\nSaldo em conta: R$ {SALDO:.2f}")
        print("=======================")

    elif opcao == "0":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação "
              "desejada.")
