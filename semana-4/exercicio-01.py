nome = str(input("Nome do funicionario:"))

salario = float(input("Salario do funicionario: R$"))

tempoDeServico = float(input("O funicionario tem quantos anos de serviço?"))

if tempoDeServico >= 5 and salario <= 2000:
    salarioFinal = salario * 1.1
    print("O salario final com 10% de aumento sera:", salarioFinal)
    
else:
    salarioFinal = salario * 1.05
    print("O salario final com aumento de 5% sera", salarioFinal)
    
