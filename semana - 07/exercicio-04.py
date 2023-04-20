quantidadePares = 0
quantidadeImpares = 0
quantidadeZeros = 0
for i in range(1, 11):
    numero = int(input("Informe um numero:"))
    if numero % 2 == 0:
        quantidadePares += 1
        
    elif numero % 2 == 1:
        quantidadeImpares += 1
        
    if numero == 0:
        quantidadeZeros += 1
        
print("Total de numeros pares:", quantidadePares, "quantidade de numeros impares:", quantidadeImpares, "e qauntidade de zeros:", quantidadeZeros)
        
    
   
    
