def somarNumero(numero):
    for i in range(0, numero):
        numero = numero + i
    return numero
        
def main():
    numero = int(input("Informe um numero:"))
    n = somarNumero(numero)
    print(n)
    
main()
