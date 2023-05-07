def menu():
    print("Bem vindo ao Banco")
    print("1 - Sacar")
    print("2- Depositar")
    print("3- Mostrar saldo")
    print("4 - Sair")
    opc = int(input("informe a opcao desejada:"))
    return opc

def realizarSaque(saldo):
    sacar = float(input("informe a quantia que deseja sacar:"))
    if sacar > saldo:
        print("Saldo Insuficiente!")
    else:
        saldo = saldo - sacar
        print("Saldo atualizado:", saldo)
    return saldo
    
def realizarDeposito(saldo):
    deposito = float(input("Informe a quantia que deseja depositar:"))
    saldo = saldo +deposito
    print("Saldo aualizado:", saldo)
    return saldo
    
def main():
    saldo = 0
    opc = 0
    while opc != 4:
        opc = menu()

        if opc == 1:
            saldo = realizarSaque(saldo)
        elif opc == 2:
            saldo = realizarDeposito(saldo)
        elif opc == 3:
            print("Seu saldo é:", saldo)
        elif opc == 4:
            print("Saindo...")
        else:
            print("Opcao invalida!!")
            
main()
