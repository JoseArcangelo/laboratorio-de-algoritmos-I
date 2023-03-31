l1 = float(input("Informe o primeiro lado do triangulo:"))

l2 = float(input("Informe o segundo lado do triangulo:"))

l3 = float(input("Informe o terceiro lado do triangulo:"))

if l1 == l2 and l1 == l3:
    print("Triângulo Equilátero: três lados iguais")

elif l1 == l2 or l1 == l3 or l3 == l2:
    print("Triângulo Isósceles: quaisquer dois lados iguais")
    
else:
    print("Triângulo Escaleno: três lados diferentes")
