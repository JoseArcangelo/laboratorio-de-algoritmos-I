totalNumeros = 0
entre30e90 = 0 

while totalNumeros < 10:
    numero = float(input("Digite um numero:"))
    totalNumeros +=1
    
    if numero > 30 and numero < 90:
        entre30e90 += 1
        
print("Dentre esse numeros digitados possui", entre30e90, "numeros entre 30 e 90")
