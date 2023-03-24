sexo = str(input("Digite e do sexo masculino ou feminino?"))

altura = float(input("Digite sua altura:"))

if sexo == "masculino":
    pesoIdeal = (72.7 * altura) - 58
    print("Seu peso ideal é", pesoIdeal)
    
else:
    pesoIdeal = (62.1 * altura) - 44.7
    print("Seu peso ideal é", pesoIdeal)
