quantidadePessoas = 0
peso = 0
idade = 0 
mediaIdade = 0
maioresDeIdade = 0
idadeEntre10e30 = 0

while quantidadePessoas < 7:
    peso += float(input("Informe o peso dessa pessoa:"))

    idade = int(input("Informe a idade dessa pessoa:"))
    
    mediaIdade += idade
    
    quantidadePessoas += 1
    
    if idade > 10 and idade < 30:
        idadeEntre10e30 += 1
        
    if idade > 18:
        maioresDeIdade += 1

mediaIdade = mediaIdade / 7
porcentagem = (idadeEntre10e30 / 7) * 100

print("A media das idades das 7 pessoas é:", mediaIdade)
print("A quantidade de pessoas maiores de idade é:", maioresDeIdade)
print("Porcentagem de pesoas entre 10 e 30 anos", porcentagem, "%")
