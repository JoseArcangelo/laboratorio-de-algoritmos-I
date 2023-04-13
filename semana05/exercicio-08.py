totalPessoas = 0
elevadorA = 0
elevadorB = 0
elevadorC = 0
while totalPessoas < 10:
    elevador = str(input("Informe qual elevador você mais utiliza(A,B ou C):")).upper()
    totalPessoas += 1
    
    if elevador == "A":
        elevadorA += 1
        
    elif elevador == "B":
        elevadorB += 1
        
    elif elevador == "C":
        elevadorC += 1

    else: 
        print("O prédio nao possui esse elevador informado!")
        
porcentagemA = (elevadorA * 100) / 10

porcentagemB = (elevadorB * 100) / 10

porcentagemC = (elevadorC * 100) / 10

print("Dentro desse grupo de 10 pessoas", elevadorA, "utilezam mais o elevador A,",
elevadorB, "utilizam o elevadorB e", elevadorC, "utilizam o C")
print("Em porcentagem", porcentagemA, "dessas 10 pessoas utilizam o elevador A,", porcentagemB, "utilizam o elevador B e", 
porcentagemC, "utilizam o C")
