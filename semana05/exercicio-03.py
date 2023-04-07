numero = 1
quantidade10 = 0

while numero != 0:
    numero = float(input("Informe um numero:"))
    
    if numero == 10:
        quantidade10 += 1 
        
print ("O numero 10 foi digitado", quantidade10, "vezes")
