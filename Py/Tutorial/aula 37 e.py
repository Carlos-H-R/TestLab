import random
gabarito = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]
mtx = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,0,14,15]]

def escolha():
    k = True
    while k:
        print("Pressione (1) para prosseguir ou (0) para desistir")
        x = input("--> ")
        if x.isdigit():
            x = int(x)
            if x == 1:
                k = False
                cdm = 1
            elif x == 0:
                print("Você desistiu!")
                k = False
                cdm = 0
            else:
                print("Comando Inválido!")
        else:
            print("Comando Inválido!")
    return cdm

def matriz():
    mtx = [0]
    base = list(range(16))
    for i in range(0,4):
        mtx.append(0)
        aux = []
        for j in range(0,4):
            x = random.choice(base)
            aux.append(x)
            base.remove(x)
        mtx[i] = aux
    for i in range(4):
        for j in range(4):
            if mtx[i][j] == 0:
                zi = i
                zj = j
    return mtx,zi,zj

def venceu(mtx):
    global gabarito

    if mtx == gabarito:
        print("Parabéns, você venceu!")
        result = 1
    else:
        result = 0
    return result

def imprima(m):
    print("")
    for i in range(4):
        print(m[i])
    print("")

def jogada(zi,zj):
    key = True
    while key:
        print("\nSelecione a peça: ")
        l = input("Linha: ")
        c = input("Coluna: ")

        if l.isdigit() and c.isdigit():
            l = int(l)
            c = int(c)
            if 0 < l < 5 and 0 < c < 5:
                l -= 1
                c -= 1
                if l == zi and (c == zj+1 or c == zj-1):
                    print("\nJogada Válida!")
                    key = False
                elif c == zj and (l == zi+1 or l == zi-1):
                    print("\nJogada Válida!")
                    key = False
                else:
                    print("\nJogada Inválida!\n")
            else:
                print("A linha e coluna deve ser um valor entre 1 e 4 inclusive.")
        else:
            print("Entrada inválida!")
    return l,c

def movimento(mtx,zi,zj,l,c):
    mtx[zi][zj] = mtx[l][c]
    mtx[l][c] = 0
    zi = l
    zj = c
    return mtx,zi,zj

def main():
    mtx,zi,zj = matriz()
    imprima(mtx)
    lock = True
    while lock:
        x = escolha()
        if x == 1:
            l,c = jogada(zi,zj)
            mtx,zi,zj = movimento(mtx,zi,zj,l,c)
            imprima(mtx)
            y = venceu(mtx)
            if y == 1:
                lock = False
        elif x == 0:
            print("Jogo encerrado!\n")
            lock = False
    input("Pressione ENTER para fechar")

main()
