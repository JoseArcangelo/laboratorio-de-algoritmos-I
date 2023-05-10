def somaImposto(taxaImposto, custo):
    valorImposto = (taxaImposto / 100) * custo
    valorFinal = valorImposto + custo
    return valorFinal


def main():
    custo = float(input("Informe o valor do produto:"))
    taxaImposto = float(input("Informe a taxa(%) de imposto do produto:"))
    valorFinal = somaImposto(taxaImposto, custo)
    print("valor final da compra:", valorFinal)
    
main()
