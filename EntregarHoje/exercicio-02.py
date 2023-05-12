def lerDados(totalIdade, maioresIdade, idade10e30):
    for i in range(7):
        idade = int(input("Informe sua idade:"))
        #peso = float(input("Informe o seu peso:"))
        totalIdade = totalIdade + idade
        if idade >= 18:
            maioresIdade += 1
        
        if idade >= 10 and idade <= 30:
            idade10e30 += 1
        
    return totalIdade, maioresIdade, idade10e30
        

def media(totalIdade):
    m = totalIdade / 7
    print("A media de idade dessas pessoas é", m)
    
def lerMaioresIdades(maioresIdade):
    print("O total de pessoas maiores de idade é", maioresIdade)

def pMaioresIdade(maioresIdade):
    p = (maioresIdade / 7) * 100
    print("Porcentagem de pessoas maiores de idade:", p)
    
    
def main():
    totalIdade = 0
    maioresIdade = 0
    idade10e30 = 0
    totalIdade, maioresIdade, idade10e30 = lerDados(totalIdade, maioresIdade, idade10e30)
    media(totalIdade)
    lerMaioresIdades(maioresIdade)
    pMaioresIdade(maioresIdade)
main()
    
