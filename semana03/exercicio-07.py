sexo = str(input("Voce é do sexo masculino ou feminino?"))

altura = float(input("Qual sua altura?"))

if sexo == "masculino":
    pesoIdeal = (72.7 * altura) - 58
    print("Seu peso ideal é", pesoIdeal)
    
else:
    pesoIdeal = (62.1 * altura) - 44.7
    print("Seu peso ideal é", pesoIdeal)
