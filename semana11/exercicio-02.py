def menu(opcao):
  print("1 - Adicionar número")
  print("2 - Remover número")
  print("3 - Ver lista")
  print("4 - Sair")
  opcao = int(input("informe a opção desejada:"))
  return opcao

def adicionarItem(lista):
  n = float(input("Informe o número que deseja adicionar a lista:"))
  lista.append(n)

def removerItem(lista):
  print("Numeros da lista:", lista)
  n = float(input("Informe o número que deseja remover da lista:"))
  
  for i in lista:
    if i == n:  
      lista.remove(n)
      
    else:
      print("A lista não possui esse número informado!")

def main():
  lista = []
  opc = 0
  while opc != 4:
    teste = 0
    while teste != 1:
      opc = menu(opc)

      if opc == 1:
        adicionarItem(lista)
        teste = 1
        
      elif opc == 2:
        removerItem(lista)
        teste = 1
        
      elif opc == 3:
        print(lista)
        teste = 1
      
      elif opc == 4:
        print("Saindo...")
        teste = 1
        
      else:
        print("Opção Inválida!!")
        
main()
