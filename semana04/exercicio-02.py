valor = float(input("Infome o valor da peça:"))

print("1- Pagamento á vista\n", "2-Pagamento em 2 vezes\n", "3- Pagamento em 3 vezes" )

opcao = int(input("Escolha uma opção:"))

if opcao == 1:
    print("Valor final da peça sendo pago á vista:", valor)
    
elif opcao == 2:
    valor = valor / 2
    print("Pagando em 2 vezes, o valor de suas parcelas será", valor)
    
elif opcao == 3:
    valor = valor / 3
    print("Pagando em 3 vezes, o valor de suas parcelas será", valor)
    
else:
    print("Opção inválida!")
