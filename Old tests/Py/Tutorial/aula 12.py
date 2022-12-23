b = int(input("Digite a base:"))
x = int(input("Digite o expoênte:"))
cont = 0
y = b

while cont < x:
    y = y*b
    cont = cont + 1

if (cont < x) == False:
    print(y)
