

def main_menu():
    main_menu = """

    ##### Seja bem vindo ao sistema bancário #####
    ##### Faça a seleção de uma opção abaixo #####

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Cadastrar usuário
    [5] Cadastrar nova conta
    [0] Sair

    """
    return input(main_menu)

def depositar(saldo, valor, extrato, /):
    
    if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação inválida, deposite um valor maior que R$ 0,00!")
        
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES_DIARIO):
        if valor > saldo:
            print("Operação inválida, valor do saque é maior que o do saldo!")
        elif valor > limite:
            print("Operação inválida, valor do saque é maior que o limite definido por saque!")
        elif numero_saques >= LIMITE_SAQUES_DIARIO:
            print("Operação inválida, limite de saques diários excedido!")
        elif valor > 0:
            saldo -= valor
            numero_saques += 1
            extrato += f"Saque: R$ {valor:.2f}\n"
        else:
            print("Operação inválida, informe um valor maior que R$0,00!")

        return saldo, extrato, numero_saques, LIMITE_SAQUES_DIARIO

def show_extrato(saldo, /, *, extrato):
     
    print("**************EXTRATO**************")
    print("Não foi realizado nenhuma operação!\n" if not extrato else extrato)
    print(f"Saldo: R$ {saldo:.2f}")
    print("***********************************")

def new_user(usuarios):
    cpf = input("Informe o CPF(somente números) para abetura da conta: ")
    usuario = users_list(cpf, usuarios)

    if usuario:
        print("Favor informar um CPF que não tenha sido cadastrado")
        return

    name = input("Informe seu nome completo: ")
    birthday = input("Informe sua data de nascimento (Ex: dd-mm-aaaa): ")
    adress = input("Informe seu endereço (Ex: rua, numero - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": name, "data_nascimento": birthday, "cpf": cpf, "endereco": adress})
    print("Cadastro realizado!")
   
def users_list(cpf, usuarios):
     lista_usuarios = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
     return lista_usuarios[0] if lista_usuarios else None
     
def new_account(agencia, numero_conta, usuarios):
     cpf = input("Informe o seu CPF: ")
     usuario = users_list(cpf, usuarios)

     if usuario:
          print("Cadastro realizado!")
          return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
     print("Cadastro não realizado! Usuário não reconhecido! ")

def head():

    LIMITE_SAQUES_DIARIO = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []


    while True:
        opcao = main_menu()
    
        if opcao == "1":
            valor = float(input("Informe o valor que será depositado: "))
            saldo, extrato = depositar(saldo, valor, extrato)    

        elif opcao == "2":
            valor = float(input("Informe o valor que será sacado: "))
            
            saldo, extrato, numero_saques, LIMITE_SAQUES_DIARIO = sacar(
             saldo=saldo,
             valor=valor,
             extrato=extrato,
             limite=limite,
             numero_saques=numero_saques,
             LIMITE_SAQUES_DIARIO=LIMITE_SAQUES_DIARIO,
         )

        elif opcao == "3":
            show_extrato(saldo, extrato=extrato)
        
        elif opcao == "4":
            new_user(usuarios)

        elif opcao == "5":
            numero_conta = len(contas) + 1
            conta = new_account(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)

    
        elif opcao == "0":
            print("Obrigado por utilizar nossos serviços!\n")
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

head()



