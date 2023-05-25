def lerLista(lista):
    for i in range(1, 11):
        lista.append(i)
    return lista
    
def lerOrdemInversa(lista):
    n = 9
    for i in range(n, -1, -1):
        print(lista[i])
        
def main():
    lista = []
    lerLista(lista)
    lerOrdemInversa(lista)
    
main()
