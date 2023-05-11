def calcular(hora):
    if hora < 12:
        hora = hora + 12
    else:
        hora = hora - 12
    return hora

def main():
    hora = int(input("Informe a hora:"))
    minutos = int(input("informe os minuto:"))
    hora = calcular(hora)
    print("Horas:", hora, "Minutos:", minutos)
main()
