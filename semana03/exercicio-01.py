horas = float(input("Quantidade de horas trabalhadas no mês:"))

salario = horas * 35

if salario <=1000:
    aumento = salario + 300
    print("Salario final com aumento sera R$", aumento)
    
else:
    print("Salario final sem aumento sera R$", salario)
