def pesquisa(sim, nao):
    for i in range(20):
        teste = 0
        while teste != 1:
            pergunta = str(input("Resposta da pesquisa(Sim/Nao):")).upper()
            if pergunta == "SIM":
                sim += 1
                teste = 1 
            elif pergunta == "NAO" or pergunta == "NÃO":
                nao += 1
                teste = 1
            else:
                print("Resposta invalida!!! responda somente com Sim ou Nao!")
    return sim, nao

def main():
    sim = 0
    nao = 0
    sim, nao = pesquisa(sim, nao)
    print("O total de pessoas que responderam Sim foi:", sim)
    print("O total de pessoas que responderam Não foi", nao)
    
main()
