import random

base = list(range(1,61))
sorte = []
result = []
base2 = base.copy()

for i in range(6):
        n = random.randint(0,len(base2)-1)
        sorte.append(base2[n])
        base2.pop(n)
sorte.sort()

print("Seu bilhete é: ",sorte)

hexa = 0
quina = 0
quadra = 0

x = 0
while x != 50063860:
    result.clear()
    base2 = base.copy()
    for i in range(6):
        ix = random.randint(0,len(base2)-1)
        result.append(base2[ix])
        base2.pop(ix)
    result.sort()
    ctr = 0
    for i in range(6):
        for j in range(6):
            if sorte[i] == result[j]:
                ctr += 1

    if ctr == 6:
        hexa += 1
    elif ctr == 5:
        quina += 1
    elif ctr == 4:
        quadra += 1

print("Foram sorteados %i megas, %i quinas e %i quadras."%(hexa,quina,quadra))
