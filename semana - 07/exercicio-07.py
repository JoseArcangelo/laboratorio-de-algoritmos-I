n1 = int(input("Informe o primeiro numero:"))

n2 = int(input("Informe o segundo numero:"))

x = 0

if n1 > n2:
   x = n1 
   n1 = n2
   n2 = x
   
for i in range(n1, n2):
    if i % 2 == 0:
        print(i)
