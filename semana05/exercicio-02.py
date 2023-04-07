saldo = float(input("Informe seu saldo atual:"))

opcao = 0

while opcao != 4:
    print("1- Sacar")
    print("2- Depositar")
    print("3- Saldo")
    print("4- Sair")
    opcao = int(input("Escolha uma das opções:"))
    
    if opcao == 1:
        sacar = float(input("Informe a quantia de dinheiro que deseja sacar:"))
        
        if saldo < sacar:
            print("Saldo insuficiente!")
            
        else:
            saldo -= sacar
            
    elif opcao == 2:
        depositar = float(input("Informe a quantia de dinheiro que deseja depositar:"))
        
        saldo += depositar
        
    elif opcao == 3:
        print("Seu saldo é R$:", saldo)
        
    elif opcao == 4:
        print("VOLTE SEMPRE!")
        
    else:
        print("Opcao inválida!")
