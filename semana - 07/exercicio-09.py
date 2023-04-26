jornalA = 0
jornalB = 0
jornalC = 0

for i in range(1, 11):
    opcao = input("Qual jornal você mais lê? Digite A, B ou C para escolher:").upper()
    if opcao == "A":
        jornalA += 1
    elif opcao == "B":
        jornalB += 1
    elif opcao == "C":
        jornalC += 1
    else:
       print("Opção inválida. Tente novamente.")



porcentagemA = (jornalA / i) * 100
porcentagemB = (jornalB / i) * 100
porcentagemC = (jornalC / i) * 100

if jornalA >= jornalB and jornalA >= jornalC:
    if jornalB >= jornalC:
        print("Em terceiro lugar ficou o jornal C com", porcentagemC, "% dos votos, em segundo lugar o jornal B com", porcentagemB, "% e em primeiro lugar o jornal A com", porcentagemA, "%")
    else:
        print("Em terceiro lugar ficou o jornal B com", porcentagemB, "% dos votos, em segundo lugar o jornal C com", porcentagemC, "% e em primeiro lugar o jornal A com", porcentagemA, "%")

elif jornalB > jornalA and jornalB >= jornalC:
    if jornalA >= jornalC:
        print("Em terceiro lugar ficou o jornal C com", porcentagemC, "% dos votos, em segundo lugar o jornal A com", porcentagemA, "% e em primeiro lugar o jornal B com", porcentagemB, "%")
    else:
        print("Em terceiro lugar ficou o jornal A com", porcentagemA, "% dos votos, em segundo lugar o jornal C com", porcentagemC, "% e em primeiro lugar o jornal B com", porcentagemB, "%")

elif jornalC > jornalA and jornalC > jornalB:   
    if jornalA >= jornalB:
        print("Em terceiro lugar ficou o jornal B com", porcentagemB, "% dos votos, em segundo lugar o jornal A com", porcentagemA, "% e em primeiro lugar o jornal C com", porcentagemC, "%")
    else:
        print("Em terceiro lugar ficou o jornal A com", porcentagemA, "% dos votos, em segundo lugar o jornal B com", porcentagemB, "% e em primeiro lugar o jornal C com", porcentagemC, "%")

        

    
