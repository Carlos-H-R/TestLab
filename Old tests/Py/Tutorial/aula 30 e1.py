import random

vidap = int(1000)
manap = int(600)

vidai = int(100)

n = int(input("Quntos inimigos deseja enfrentar?"))

enemy = []

for i in range(0,n):
        enemy.append(vidai)

while vidap > 0 or enemy.count(0) < n:

    print("\nVida: %i \nMana: %i"%(vidap,manap))
    print("")

    ck = True
    while ck:
        cmd = int(input("1 para atacar ou 2 para curar: "))

        if cmd == 1:
            count = 0
            for i in range(0,n):
                a = random.randint(10,15)
                print("Você causou %i de dano ao inimigo %i."%(a,i+1))
                enemy[i] = enemy[i] - a
                if enemy[i] <= 0:
                    enemy[i] = 0
            ck = False

        elif cmd == 2:
            h = random.randint(10,20)
            vidap = vidap + h
            if vidap >= 1000:
                vidap = 1000
            ck = False

        else:
            print("Comando Inválido!")

    print("")

    if enemy.count(0) < n:
        for i in range(0,n):
            if enemy[i] > 0:
                eatk = random.randint(1,5)
                vidap = vidap - eatk
                print("O inimigo %i causou %i de dano."%(i+1,eatk))
                if vidap <=  0:
                    vidap = 0
            elif enemy[i] == 0:
                print("Inimigo %i abatido."%(i+1))
        
        
            
        
