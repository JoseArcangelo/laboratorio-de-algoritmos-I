def lerNumeros(listaNumeros):
    for i in range(5):
        n = int(input("Informe um valor inteiro:"))
        listaNumeros.append(n)

def verificarNumero(listaNumeros):
    n = int(input("Informe o numero que deseja ver se tem na lista:"))
    verdade = 0
    for i in listaNumeros:
        if i == n:
            verdade += 1
            
    if verdade >= 1:
        print("Esse número ESTA na lista")
        
    else:
        print("Esse número NÃO esta na lista")
        

def main():
    listaNumeros = []
    lerNumeros(listaNumeros)
    verificarNumero(listaNumeros)
    
main()
