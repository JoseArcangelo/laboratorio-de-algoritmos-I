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
        
elevadorA = (elevadorA * 100) / 10

elevadorB = (elevadorB * 100) / 10

elevadorC = (elevadorC * 100) / 10

print("Dentre as 10 pessoas", elevadorA, "% utilizam o elevador A,", elevadorB, "% utilizam o elevador B e", elevadorC, "% utilizam o elevador C.")
