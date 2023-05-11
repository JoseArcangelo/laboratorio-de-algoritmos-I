def calcularDecimetros(valorMetros):
    decimetros = valorMetros * 10
    return decimetros

def calcularCentimetros(valorMetros):
    centimetros = valorMetros * 100
    return centimetros
    
def calcularMilimetros(valorMetros):
    milimetros = valorMetros * 1000
    return milimetros

def main():
    valorMetros = float(input("Informe um valor em metros:"))
    valorDecimetros = calcularDecimetros(valorMetros)
    valorCentimetros = calcularCentimetros(valorMetros)
    valorMilimetros = calcularMilimetros(valorMetros)
    print("Valor em decimetros:", valorDecimetros, "Centimetros", valorCentimetros, "Milimetros:", valorMilimetros)
    
main()
    
