opcao = 0
idade = 0
altura = 0
totalPessoas = 0

while opcao != 3:
    print("1- Cadastrar pessoa")
    print("2-Mostrar media parcial de altura e idade")
    print("3- Sair")
    opcao = int(input("Escolha uma opção:"))
    
    if opcao == 1:
        totalPessoas += 1

        idade += int(input("Informe a sua idade:"))
        mediaIdade = idade / totalPessoas
        
        altura += float(input("Informe a sua altura:"))
        mediaAltura = altura / totalPessoas
        
        
    elif opcao == 2:
        print("A media parcial de idade é", mediaIdade, "e a de altura é", mediaAltura)
        
        
    elif opcao == 3:
        print("A media de idade final e oficial é", mediaIdade, "e a de alutra é", mediaAltura)
        print("Saindo...")
        
    else:
        print("Opção inválida!")
    
        
