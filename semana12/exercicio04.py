def lerListas(lista01, lista02):
    print("Informe três numeros na lista 1")
    for i in range(3):
        n = int(input("Informe um valor:"))
        lista01.append(n)
        
    print("Informe três numeros na lista 2")
    for i in range(3):
        n = int(input("Informe um valor:"))
        lista02.append(n)

def somarElementos(lista01, lista02, lista03):
    for a in range(len(lista01)):
        x = lista01[a] + lista02[a]
        lista03.append(x)
    return lista03  
    
def main():
    lista01 = []
    lista02 = []
    lista03 = []
    lerListas(lista01, lista02)
    lista03 = somarElementos(lista01, lista02, lista03)
    print(lista03)

main()
