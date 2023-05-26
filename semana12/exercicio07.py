import random

def lerNumeros(lista):
    for i in range(10):
        n = random.randint(1, 50)
        lista.append(n)
    return lista
    
def parimpar(lista, totalPares, totalImpares):
    for i in lista:
        if i % 2 == 0:
            totalPares+= 1
            
        else:
            totalImpares += 1
            
    return totalPares, totalImpares
    
def main():
    lista = []
    totalPares = 0
    totalImpares = 0
    lerNumeros(lista)
    totalPares, totalImpares = parimpar(lista, totalPares, totalImpares)
    print("Numeros da lista", lista)
    print("Total de numeros pares:", totalPares)
    print("Total de numeros impares:", totalImpares)
    
main()
