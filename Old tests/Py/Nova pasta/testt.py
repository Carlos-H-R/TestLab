def printmat(vet):
    for i in vet:
        print(i)

def createMat(x):
    vet = []
    for i in range(x):
        aux = []
        for j in range(x):
            aux.append(0)
        vet.append(aux)
    return vet
    

def printPattern(k):
    m = (2*k)-1
    mat = createMat(m)
    i = 0
    f = m

    for c in range(k,0,-1):
        for a in range(i,f):
            for b in range(i,f):
                mat[a][b] = c
        i += 1
        f -= 1

    printmat(mat)


n = int(input("--> "))
printPattern(n)
