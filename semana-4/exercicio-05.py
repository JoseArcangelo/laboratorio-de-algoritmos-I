respostasPositivas = 0

p1 = str(input("Telefonou para a vitima?(Sim/Não)")).upper()

if p1 == "SIM":
    respostasPositivas += 1
    
p2 = str(input("Esteve no local do crime?(Sim/Nao)")).upper()

if p2 == "SIM":
    respostasPositivas += 1
    
p3 = str(input("Mora perto da vitima?(Sim/Não)")).upper()

if p3 == "SIM":
    respostasPositivas += 1
    
p4 = str(input("Devia para a vitima?(Sim/Não)")).upper()

if p4 == "SIM":
    
    respostasPositivas += 1
    
p5 = str(input("Já trabalhou com a vitima?(Sim/Não)")).upper()

if p5 == "SIM":
    
    respostasPositivas += 1
    
if respostasPositivas == 2:
    print("SUSPEITO!")
        
elif respostasPositivas >= 3 and respostasPositivas <= 4:
    print("CÚMPLICE!")
        
elif respostasPositivas == 5:
    print("ASSASSINO!")
        
else:
    print("INOCENTE!")
        
        
