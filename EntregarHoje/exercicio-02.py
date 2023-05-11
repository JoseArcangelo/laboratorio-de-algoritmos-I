def menu():
    print("1 - Cadastrar pessoa")
    print("2- Mostrar media parciais")
    print("3- Sair")
    opcao = int(input("Opcao:"))
    return opcao

def cadastraPessoa(somaIdades, somaAlturas):
    idade = int(input("Informe a idade:"))
    altura = float(input("Informe a altura:"))
    
    somaIdades = somaIdades + idade
    somaAlturas = somaAlturas + altura
    
    return somaIdades, somaAlturas
    
def mediaParcial(somaIdades, somaAlturas, qtdPessoas):
    print("Media das idades:", somaIdades/qtdPessoas)
    print("Media das alturas:", somaAlturas/qtdPessoas)
    
def main():
    opc = 0
    somaIdades = 0
    somaAlturas = 0
    qtdPessoas = 0
    while opc != 3:
        opc = menu()
        
        if opc == 1:
            somaIdades, somaAlturas = cadastraPessoa(somaIdades, somaAlturas)
            qtdPessoas += 1
            
        elif opc == 2:
            mediaParcial(somaIdades, somaAlturas, qtdPessoas)
            
        elif opc == 3:
            mediaParcial(somaIdades, somaAlturas, qtdPessoas)
    
main()
