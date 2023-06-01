def lerNumeros(lista):
    for i in range(5):
        n = float(input("Digite um valor:"))
        lista.append(n)
    return lista
        
def maiorMenorNumero(lista):
    maiorNumero = lista[0]
    menorNumero = lista[0]
    posicaoMaior = 0
    posicaoMenor = 0
    contador = 0
    for i in lista:
        if i > maiorNumero:
            maiorNumero = i
            posicaoMaior = contador
            
        elif i < menorNumero:
            menorNumero = i
            posicaoMenor = contador
            
        contador += 1
        
    print("Maior numero da lista:", maiorNumero, ", e sua posicao:", posicaoMaior)
    print("Maior numero da lista:", menorNumero, ", e sua posicao:", posicaoMenor)    

def main():
    lista = []
    lerNumeros(lista)
    maiorMenorNumero(lista)
    
main()
