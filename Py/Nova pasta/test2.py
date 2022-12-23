l = int(input("Insira o numero de linhas: "))
c = int(input("Insira o número de colunas: "))
m = []*l
for i in range(0,l):
    m[i] = []*c
    for j in range(0,c):
        m[i][j] = input("digite o valor da célula")
print(m)

