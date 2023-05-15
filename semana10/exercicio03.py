def lerNumero():
    numero = float(input("Informe um numero:"))
    return numero

def lerDobro(numero):
    dobro = numero * 2
    return dobro
    
def main():
    numero = lerNumero()
    dobro = lerDobro(numero)
    print("O dobro de", numero, "é", dobro)

main()
