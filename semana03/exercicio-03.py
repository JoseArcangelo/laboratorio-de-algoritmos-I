anoDeNascimento = int(input("Digite seu ano de nascimento:"))

idade = 2023 - anoDeNascimento

print("Sua idade é", idade, "anos")

if idade >= 16:
    print("Voce já pode votar!")
else:
    print("Voce ainda não pode votar!")
