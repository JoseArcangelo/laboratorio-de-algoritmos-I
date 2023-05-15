###F = C x 1,8 + 32

def lerCelsius():
    tCelsius = float(input("Informe a temperatura em Celsius:"))
    return tCelsius

def calcularFahrenheit(tCelsius):
    tFahrenheit = tCelsius * 1.8 + 32
    return tFahrenheit
    

def main():
    tCelsius = lerCelsius()
    tFahrenheit = calcularFahrenheit(tCelsius)
    print("A temperatura em Fahrenheit será", tFahrenheit)
    
main()

