quantidadePessoas = 0
peso = 0
idade = 0 
maioresDeIdade = 0
idadeEntre10e30 = 0
porcentagem = 0
mediaIdade = 0
while quantidadePessoas < 7:
    quantidadePessoas += 1

    peso = float(input("Informe o peso dessa pessoa:"))

    idade = int(input("Informe a idade dessa pessoa:"))
    mediaIdade += idade

    if idade > 10 and idade < 30:
        idadeEntre10e30 += 1
        porcentagem = (idadeEntre10e30 / quantidadePessoas) * 100
        
    if idade >= 18:
        maioresDeIdade += 1
        
mediaIdade = mediaIdade / quantidadePessoas

print("A media das idades das 7 pessoas é:", mediaIdade)
print("A quantidade de pessoas maiores de idade é:", maioresDeIdade)
print("Porcentagem de pesoas entre 10 e 30 anos", porcentagem, "%")
