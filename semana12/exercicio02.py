def lerNumeros(lista):
    for i in range(5):
        n = float(input("Informe um valor:"))
        lista.append(n)
    return lista    
    
def somaLista(lista, soma, media):
    for i in lista:
        soma = soma + i
    media = soma / 5
    return soma, media
    
def main():
    soma = 0
    media = 0
    lista = []
    lerNumeros(lista)
    soma, media = somaLista(lista, soma, media)
    print("Soma da lista:", soma)
    print("Media da lista:", media)
main()
