def calcularValor(totalLaranjas):
    if totalLaranjas <= 12:
        valorPagar = totalLaranjas * 0.40
    else:
        valorPagar = totalLaranjas * 0.25
    return valorPagar
    
def main():
    totalLaranjas = int(input("Informe o total de laranjas:"))
    valorPagar = calcularValor(totalLaranjas)
    print("O valor a ser pago será:", valorPagar)

main()
