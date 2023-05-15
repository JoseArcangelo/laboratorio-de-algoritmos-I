def lerRespostas(jA, jB, jC):
    for i in range(10):
        teste = 0
        while teste != 1:
            resposta = str(input("Informe qual destes jornais voce mais lê (A, B ou C):")).upper()
            if resposta == "A":
                jA += 1
                teste = 1
                
            elif resposta == "B":
                jB += 1
                teste = 1
                
            elif resposta == "C":
                jC += 1
                teste = 1
                
            else:
                print("Resposta inválida!!!!")
                
    return jA, jB, jC

def porcentagem(jA, jB, jC):
    jA = (jA / 10) * 100
    jB = (jB / 10) * 100
    jC = (jC / 10) * 100
    return jA, jB, jC
    
def resultado(jA, jB, jC):
    if jA >= jB and jA >= jC:
        if jB >= jC:
            print("Em terceiro lugar ficou o jornal C com", jC, "% dos votos, em segundo lugar o jornal B com", jB, "% e em primeiro lugar o jornal A com", jA, "%")
        else:
            print("Em terceiro lugar ficou o jornal B com", jB, "% dos votos, em segundo lugar o jornal C com", jC, "% e em primeiro lugar o jornal A com", jA, "%")

    elif jB > jA and jB >= jC:
        if jA >= jC:
            print("Em terceiro lugar ficou o jornal C com", jC, "% dos votos, em segundo lugar o jornal A com", jA, "% e em primeiro lugar o jornal B com", jB, "%")
        else:
            print("Em terceiro lugar ficou o jornal A com", jA, "% dos votos, em segundo lugar o jornal C com", jC, "% e em primeiro lugar o jornal B com", jB, "%")

    elif jC > jA and jC > jB:   
        if jA >= jB:
            print("Em terceiro lugar ficou o jornal B com", jB, "% dos votos, em segundo lugar o jornal A com", jA, "% e em primeiro lugar o jornal C com", jC, "%")
        else:
            print("Em terceiro lugar ficou o jornal A com", jA, "% dos votos, em segundo lugar o jornal B com", jB, "% e em primeiro lugar o jornal C com", jC, "%")

def main():
    jA = 0
    jB = 0
    jC = 0
    jA, jB, jC = lerRespostas(jA, jB, jC)
    jA, jB, jC = porcentagem(jA, jB, jC)
    resultado(jA, jB, jC)
    
main()
