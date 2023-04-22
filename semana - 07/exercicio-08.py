fora = 0
dentro = 0

for i in range(1, 11):
    i = int(input("Informe um numero:"))
    if i > 10 and i < 20:
        dentro += 1
        
    else:
        fora += 1
        
print("Dentre esses", (fora + dentro), "numeros", dentro, "estão entre 10 e 20 e", fora, "estao fora")
        
