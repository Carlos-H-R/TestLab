m = []

print("Digite a casisa do jogador votado, de 1 a 23.")

x = 1
while x != 0:
    x = input("--> ")
    if x.isdigit():
        x = int(x)
        if 0 < x < 24 :
            m.append(x)
            print("")

        elif x == 0:
            print("Lista encerrada!")
            print("")

        else:
            print("Entrada Inválida!")
            print("")

    else:
        print("Entrada inválida!")
        print("")


print("Total de votos é %i."%(len(m)))
print("")

for i in range(1,24):
    n = m.count(i)
    p = m.count(i)%len(m)
    print("O camisa %2i recebeu %3i votos com percentual de %5.2f%%."%(i,m.count(i),p))

print("")
best = 0
votos = 0
for i in range(1,24):
    if m.count(i) > votos:
        best = i
        votos = m.count(i)
pe = votos%len(m)

print("O melhor jogador da partida foi o camisa %i, com %i votos e um percentual de %5.2f%%"%(best,votos,pe))
