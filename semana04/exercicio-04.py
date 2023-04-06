n1 = float(input("Digite um valor:"))

n2 = float(input("Digite outro valor:"))

print("1- Somar os valores")
print("2- Subtrair os valores")
print("3- Multiplicar os valores")
print("4- Dividir os valores")

opcao = int(input("Escolha uma opçao:"))

if opcao == 1:
    resposta = n1 + n2
    print("Somando os dois valores a resposta final será", resposta)

elif opcao == 2:
    resposta = n1 - n2
    print("Subtraindo os dois valores a resposta final sera", resposta)
    
elif opcao == 3 :
    resposta = n1 * n2
    print("Multiplicando os dois valores a resposta final será", resposta)
    
elif opcao == 4:
    resposta = n1 / n2
    print("Dividindo os dois valores a resposta final será", resposta)
    
else:
    print("Opção inválida!")
