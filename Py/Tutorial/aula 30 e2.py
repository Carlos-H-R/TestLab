notas = []
print("\nInsira o valor de cada nota. \nPara encerrar digite '-1' \n")

key = True
while key:
    k = True
    while k:
        n = (input("--> "))
        if n == '-1':
            print("\nLista encerrada!\n")
            key = False
            k = False
        try:
            n = float(n)
            if 0 <= n <= 10:
                notas.append(n)
                k = False
            else:
                print("\nVocê deve inserir um número válido!\n")
        except:
            print("\nVocê deve inserir um número válido!\n")

print("\nForam computados %i valores\n"%(len(notas)))
print(notas)
print("")

notas.reverse()
total = 0
for i in range(0,len(notas)):
    print(notas[i])
    total += notas[i]

media = total/len(notas)

print("\nA soma das notas é %.1f."%(total))
print("\nA média das notas é %.1f."%(media))

acima = 0
sete = 0
for i in range(0,len(notas)):
    if notas[i] > media:
        acima += 1
    if notas[i] < 7:
        sete += 1

print("\n%i das notas estão acima da média"%(acima))
print("\n%i das notas estão abaixo de sete"%(sete))

print("\nPrograma encerrado!\n")

input("Pressione ENTER para fechar")
