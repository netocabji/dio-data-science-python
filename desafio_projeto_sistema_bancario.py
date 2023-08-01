print("##### Seja bem vindo ao sistema bancário #####")
menu = '''

##### Faça a seleção de uma opção abaixo #####

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

'''

saldo = 0
limite_por_saque = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES_DIARIO = 3

while True:

    opcao = input(menu)

    print("")
    
    if opcao == "1":
        print("Opção depositar selecionada!", "\n")
        valor = float(input("Informe o valor que será depositado: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Operação inválida, deposite um valor maior que R$ 0,00!")
            

    elif opcao == "2":
        print("Opção saque selecionada!" "\n")
        valor = float(input("Informe o valor que será sacado: "))
        if valor > saldo:
            print("Operação inválida, valor do saque é maior que o do saldo!")
        elif valor > limite_por_saque:
            print("Operação inválida, valor do saque é maior que o limite definido por saque!")
        elif numero_saques >= LIMITE_SAQUES_DIARIO:
            print("Operação inválida, limite de saques diários excedido!")
        elif valor > 0:
            saldo -= valor
            numero_saques += 1
            extrato += f"Saque: R$ {valor:.2f}\n"
        else:
            print("Operação inválida, informe um valor maior que R$0,00!") 

    elif opcao == "3":
        print("**************EXTRATO**************")
        print("Não foi realizado nenhuma operação!\n" if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        print("***********************************")
    
    elif opcao == "0":
        print("Obrigado por utilizar nossos serviços!\n")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

