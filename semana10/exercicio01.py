def somarNumeros(a, b, r):
    r = a + b
    return r
    
def main():
    r = 0
    a = int(input("Informe um numero:"))
    b = int(input("Informe outro numero:"))
    r = somarNumeros(a, b, r)
    print("A soma de", a, "+", b, "é igual a", r)
    
main()
