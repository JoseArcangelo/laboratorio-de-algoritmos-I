sexoMasculino = 0
sexoFeminino = 0
olhosAzuis = 0
olhosVerdes = 0
olhosCastanhos = 0
cabeloLoiro = 0
cabeloCastanho = 0
cabeloPreto = 0
maiorIdade = 0
fivl = 0

for i in range(1, 3):
    certo = 0

    while certo == 0:
        sexo = str(input("Informe o seu sexo - M (masculino) e F (feminino):")).upper()
        
        if sexo == "M":
            sexoMasculino +=1
            certo = 1
        
        elif sexo == "F":
            sexoFeminino += 1
            certo = 1
            
        else:
            print("Opcao invalida! informe somente uma das opcoes da pergunta")

    while certo == 1:
        corOlhos = str(input("Informe a cor de seus olhos -A (azuis), V (verdes) e C (castanhos):")).upper()
        if corOlhos == "A":
            olhosAzuis += 1
            certo = 2
    
        elif corOlhos == "V":
            olhosVerdes +=1
            certo = 2
    
        elif corOlhos == "C":
            olhosCastanhos += 1
            certo = 2
            
        else:
            print("Opcao invalida! informe somente uma das opcoes da pergunta")
            
    while certo == 2:
        corCabelos = str(input("Informe a cor de seu cabelo: L (loiros), C (castanhos) e P (pretos)")).upper()
        
        if corCabelos == "L":
            cabeloLoiro += 1
            certo = 3
            
        elif corCabelos == "C":
            cabeloCastanho +=1
            certo = 3
            
        elif corCabelos == "P":
            cabeloPreto += 1
            certo = 3
            
        else:
            print("Opcao invalida! informe somente uma das opcoes da pergunta")
            
    idade = int(input("Informe a sua idade:"))
    
    if i == 1:
        maiorIdade = idade

    if idade > maiorIdade:
        maiorIdade = idade
        
    if sexo == "F" and idade > 18 and idade < 35 and corOlhos == "V" and corCabelos == "L":
        fivl += 1
        print(fivl)

      
        
    
    
        
            
        
        
