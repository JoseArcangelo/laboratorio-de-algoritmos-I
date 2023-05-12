def lerRespostas(totalA, totalB, totalC):
    totalPessoas = 0
    while totalPessoas != 10:
        teste = 0
        while teste != 1:
            entrevistar = str(input("Informe o elevador que voce mais utiliza (A, B ou C):")).upper()
            totalPessoas += 1
            if entrevistar == "A":
                totalA += 1
                teste = 1
                
            elif entrevistar == "B":
                totalB += 1
                teste = 1
            
            elif entrevistar == "C":
                totalC += 1
                tete = 1
            
            else:
                print("Resposta invalida!!! Por favor responda com alguma das opcoes que estao na pergunta!!")
                
            
    return totalA, totalB, totalC

def porcentagens(totalA, totalB, totalC):
    pA = (totalA / 10) * 100
    pB = (totalB / 10) * 100
    pC = (totalC / 10) * 100
    return pA, pB, pC

def main():
    totalA = 0
    totalB = 0
    totalC = 0
    totalA, totalB, totalC = lerRespostas(totalA, totalB, totalC)

    pA, pB, pC = porcentagens(totalA, totalB, totalC)
    
    print("Total de pessoas que escolheram o elevador A:", totalA, "e seu percentual:", pA, "%")
    print("Total de pessoas que escolheram o elevador B:", totalB, "e seu percentual:", pB, "%")
    print("Total de pessoas que escolheram o elevador C:", totalC, "e seu percentual:", pC, "%")

main()
