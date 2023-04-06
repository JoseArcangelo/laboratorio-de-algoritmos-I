n1 = float(input("Informe a primeira nota parcial do aluno:"))

n2 = float(input("Informe a segunda nota parcial do aluno:"))

m = (n1 + n2) / 2

if m >=9 and m <=10:
    print("A primeira nota do aluno é", n1, ",a segunda é", n2, " e sua media é", m)
    print("O conceito do aluno será = A")
    print("O aluno está APROVADO!")
    
elif m >= 7.5 and m < 9:
    print("A primeira nota do aluno é", n1, ",a segunda é", n2, " e sua media é", m)
    print("Com isso o conceito do aluno será = B")
    print("O aluno está APROVADO!")
    
elif m >= 6 and m < 7.5:
    print("A primeira nota do aluno é", n1, ",a segunda é", n2, " e sua media é", m)
    print("Com isso o conceito do aluno será = C")
    print("O aluno está APROVADO!")
    
elif m >= 4 and m < 6:
    print("A primeira nota do aluno é", n1, ",a segunda é", n2, " e sua media é", m)
    print("Com isso o conceito do aluno será = D")
    print("O aluno está REPROVADO!")
    
else:
    print("A primeira nota do aluno é", n1, ",a segunda é", n2, " e sua media é", m)
    print("Com isso o conceito do aluno será = E")
    print("O aluno está REPROVADO!")

