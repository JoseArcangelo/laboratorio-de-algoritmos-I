def menu():
    print("1 - Inserir item")
    print("2 - Listar itens")
    print("3 - Retirar item")
    print("4 - Retirar todos os itens")
    print("5 - Sair")
    opcao = int(input("Informe a opcao desejada:"))
    return opcao

def inserirItem(lista):
    n = float(input("Informe o numero que quer ADICIONAR a lista:"))
    if n % 2 != 0:
        print("ERRO!! INFORME SOMENTE NUMEROS PARES")
        return

    else:
        lista.append(n) 
        print("LISTA ATUALIZADA:", lista)
    return lista
        
def removerItem(lista):
    for i in lista:
        print("-", i)
    n = float(input("Informe o numero que deseja REMOVER da lista:"))
    lista.remove(n)
    print("LISTA ATUALIZADA:", lista)
    return lista

def removerTodosItens(lista):
    lista.clear()
    print("TODOS OS ITENS FORAM REMOVIDOS DA LISTA!!")
    return lista

def main():
    opc = 0
    lista = []
    
    while opc != 5:
        teste = 0
        while teste != 1:
            opc = menu()

            if opc == 1:
                inserirItem(lista)
                teste = 1
                
            elif opc == 2:
                print("Numeros da lista:")
                for i in lista:
                    print("-", i)
                teste = 1

            elif opc == 3:
                removerItem(lista)
                teste = 1
                
            elif opc == 4:
                 removerTodosItens(lista)
                 teste = 1

            elif opc == 5:
                print("Saido...")
                teste = 1
                
            else:
                print("OPÇÃO INVÁLIDA!!")
main()
