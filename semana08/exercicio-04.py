def lerNotas():
    nota = 0
    for i in range(5):
        nota += float(input("informe suas notas:"))
    nota = nota / 5
    media = nota
    return media

def resultado(media):
    if media >= 7:
        print("O aluno está APROVADO!!")
    elif media < 7 and media >= 4:
        print("O aluno ficou de RECUPERAÇÃO")
    else:
        print("O aluno está REPROVADO!!")

def main():
    media = lerNotas()
    resultadoFinal = resultado(media)

main()
