def calcularDobroTriplo(numero):
    dobro = numero * 2
    triplo = numero * 3
    return dobro, triplo

def main():
    numero = int(input("Informe o valor desejado:"))
    dobro, triplo = calcularDobroTriplo(numero)
    print("O dobro de", numero, 'é', dobro, "e o triplo é", triplo)
main()
