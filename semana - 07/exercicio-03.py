n1 = 0
n2 = 1

for x in range(10):
    x = n1 + n2
    n2 = n1
    n1 = x
    print(x)
