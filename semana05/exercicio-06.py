totalPessoas = 0
maioresDeIdade= 0 

while totalPessoas < 10:
    idade = int(input("Infome a idade da pessoa:"))
    totalPessoas += 1
    
    if idade >= 18:
        maioresDeIdade += 1
               
print("Esse grupo de", totalPessoas, "pessoas possui", maioresDeIdade, "maiores de idade!")
        
