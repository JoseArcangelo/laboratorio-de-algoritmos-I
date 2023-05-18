def lerNumero():
    numero = int(input("Informe um numero:"))
    return numero
    
def verificar(numero):
    if numero % 2 == 1 or numero == 2:
        print("True")
        
    else:
        print("False")

def main():
    numero = lerNumero()
    primo = verificar(numero)
    
main()
