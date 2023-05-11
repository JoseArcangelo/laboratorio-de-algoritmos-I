def calcular(hora):
    if hora == 0:
        hora = 12
    elif hora > 12:
        hora = hora - 12
    return hora

def main():
    hora = int(input("Informe a hora:"))
    minutos = int(input("Informe os minutos:"))
    hora = calcular(hora)
    if hora < 12:
        periodo = "A.M."
    else:
        periodo = "P.M."
    print("Horas: ", hora, ":", minutos, "no periodo-", periodo)

main()

