jornalA = 0
jornalB = 0
jornalC = 0

for i in range(0, 20):
    opcao = input("Dentre os jornais A, B e C, qual você mais lê?").upper()
    if opcao == "A":
        jornalA += 1
    elif opcao == "B":
        jornalB += 1
    elif opcao == "C":
        jornalC += 1
    else:
       print("Resposta invàlida!")
       
    print(i)

porcentagemA = (jornalA / 20) * 100
porcentagemB = (jornalB / 20) * 100
porcentagemC = (jornalC / 20) * 100

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

    
