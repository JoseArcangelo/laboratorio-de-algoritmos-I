def lerNumeros(numeros):
    for i in range(2):
        n = int(input("informe um numero:"))
        numeros.append(n)
        
    return numeros

def maiorCem(numeros, qMaiores100):
    for i in numeros:
        if i > 100:
            print(i)
            qMaiores100 += 1
        
    print("Quantidade de numeros maiores que 100:", qMaiores100)



def main():
    qMaiores100 = 0
    numeros = []
    lerNumeros(numeros)
    maiorCem(numeros, qMaiores100)

main()
