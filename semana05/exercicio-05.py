totalPessoas = 0
mediaSalario = 0
mulhereSalario100 = 0
maiorIdade = 0
menorIdade = 0

while totalPessoas < 10:
    totalPessoas += 1
    salario = float(input("Informe o SALARIO da nova pessoa participante da pesquisa:"))
    mediaSalario =mediaSalario + salario 
    sexo = str(input("Informe o SEXO da nova pessoa participante da pesquisa(Masculino/Feminino):")).upper()
    
    if sexo == "FEMININO" and salario <= 100:
        mulhereSalario100 += 1
        print(mulhereSalario100)
    
    idade = int(input("Informe a IDADE da nova pessoa participante da pesquisa:"))
    print("Total de pessoas entrevistadas:", totalPessoas)

    if menorIdade == 0 or maiorIdade == 0:
        menorIdade += idade
        maiorIdade += idade
        
    elif idade < menorIdade:
        menorIdade = menorIdade - menorIdade
        menorIdade += idade
        
    elif idade > maiorIdade:
        maiorIdade = maiorIdade - maiorIdade
        maiorIdade += idade
    

mediaSalario = mediaSalario / totalPessoas
      
print("A media de salario desse grupo de 10 pessoas é", mediaSalario)
print("A maior idade desse grupo é", maiorIdade, "e a menor idade é", menorIdade)
print("A quantidade de mulheres com sálario de ate R$100,00 é:", mulhereSalario100)

