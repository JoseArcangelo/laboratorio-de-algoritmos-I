import random

def lerNumeros(lista):
    aleatorio = 0
    for i in range(10):
        n = random.randint(1, 100)
        print(n)
        lista.append(n)
    return lista

def lerPares(lista, listaPares):
    for i in lista:
        if i % 2 == 0:
            listaPares.append(i)
            
    return listaPares
    
def main():
    lista = []
    listaPares = []
    lerNumeros(lista)
    lerPares(lista, listaPares)
    print("Lista dos numeros aleatórios:", lista)
    print("Lista desses numeros aleatórios que são pares:", listaPares)
    
main()
