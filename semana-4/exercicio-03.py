n1 = float(input("Informe a primeira nota do aluno:"))

n2 = float(input("Informe a segunda nota do aluno:"))

media = (n1 + n2) / 2

frequencia = float(input("Informe o percentual(%) de frequencia do aluno:"))



if media >= 7 and frequencia >= 75:
    print("O aluno esta APROVADO!, com media", media, "e frequenica de", frequencia, "%")
    
elif media >=4 and media < 7 and frequencia > 75:
    print("O aluno ficou de exame!, com media", media, "e frequencia de", frequencia, "%")
    
else:
    print("O aluno esta REPROVADO!, com media", media, "e frequencia de", frequencia, "%")
