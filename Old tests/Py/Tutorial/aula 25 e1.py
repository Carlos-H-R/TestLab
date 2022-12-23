notas = []

for i in range(0,4):
    notas.append(float(input("Digite a nota #%i: "%(i+1))))

print("")

for i in range(0,4):
    print("A nota #%i é %.1f"%((i+1),notas[i]))

soma = 0
for i in range(0,4):
    soma += notas[i]

media = soma/4

print("A média das notas é %.1f"%media)
