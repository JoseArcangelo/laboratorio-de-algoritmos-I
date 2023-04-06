carteira = str(input("Qual o tipo de sua carteira(A, B, C, D ou E)?")).upper()

if carteira == "A":
    print("Você pode dirigir motos e triciclos!")
    
elif carteira == "B":
    print("Você pode dirigir carros de passeio!")
    
elif carteira == "C":
    print("Você pode dirigir veiculos de carga acima de 3,5 ton")
    
elif carteira == "D":
    print("Você pode dirigir veiculos com mais de 8 passageiros")

elif carteira == "E":
    print("Você pode dirigir veiculos com unidade acoplada acima de 6 ton")
    
else:
    print("Tipo de carteira não consta na pergunta!")
