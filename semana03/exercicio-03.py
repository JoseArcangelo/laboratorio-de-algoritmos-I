anoDeNascimento = int(input("Digite seu ano de nascimento:"))

idade = 2023 - anoDeNascimento

print("Sua idade é", idade, "anos")

if idade >= 16:
    print("Voce ja pode votar!")
else:
    print("Voce ainda nao pode votar!")
