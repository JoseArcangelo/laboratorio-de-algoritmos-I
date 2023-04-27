fora = 0
dentro = 0

for i in range(0, 10):
    i = int(input("Informe um numero:"))
    if i > 10 and i < 20:
        dentro += 1
        
    else:
        fora += 1
        
print("Dentre esses numeros informados", dentro, "estão entre 10 e 20, e", fora, "estao fora")
