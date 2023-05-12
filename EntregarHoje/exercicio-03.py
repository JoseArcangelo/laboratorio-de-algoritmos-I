def lerDados(menorIdade, maiorIdade, mulheresSalario, mediaSalario):
    totalSalarios = 0
    for i in range(10):
        idade = int(input("Informe a sua idade:"))
        if i == 0:
            menorIdade = idade
            maiorIdade = idade
        
        if idade > maiorIdade:
            maiorIdade = idade
        
        if idade < menorIdade:
            menorIdade = idade
            
        sexo = str(input("Informe o seu sexo:(M/F)")).upper()
        salario = float(input("Informe seu salario:"))
        totalSalarios = totalSalarios + salario
       
        if sexo == "F" and salario <= 100:
            mulheresSalario += 1
            
    mediaSalario = media(totalSalarios)
    
    return maiorIdade, menorIdade, mulheresSalario, mediaSalario
    
            
def media(totalSalarios):
    media = totalSalarios / 10
    return media
    
def dadosIdades(menorIdade, maiorIdade, mulheresSalario):
    print("A menor idade desse grupo:", menorIdade)
    print("A maior idade desse grupo:", maiorIdade)
    print("Quantidade de mulheres com salário até R$100,00:", mulheresSalario)
            
def main():
    menorIdade = 0
    maiorIdade = 0
    mulheresSalario = 0
    mediaSalario = 0
    maiorIdade, menorIdade, mulheresSalario, mediaSalario = lerDados(menorIdade, maiorIdade, mulheresSalario, mediaSalario)
    print("A media de salario do grupo é", mediaSalario)
    dadosIdades(menorIdade, maiorIdade, mulheresSalario)
    
main()
