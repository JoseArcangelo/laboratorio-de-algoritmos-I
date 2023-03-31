veiculo = str(input("Qual veiluco voce pode dirigir?"))

tipoCarteira = str(input("Qual o tipo de sua carteira de motorista?(A,B,C,D ou E)")).upper()

if tipoCarteira == "A":
    print("Voce pode dirigir motos e triciclos")
    
elif tipoCarteira == "B":
    print("Voce pode dirigir")
