n1 = float(input("Informe a primeira nota:"))

n2 = float(input("Informe a segunda nota:"))

media = (n1 + n2) / 2

frequencia = float(input("Informe sua % se frequencia:"))



if media >= 7 and frequencia >= 75:
    print("O aluno esta aprovado!")
    
elif media >=4 and media < 7 and frequencia > 75:
    print("O aluno ficou de exame!")
    
else:
    print("Reprovado!")

