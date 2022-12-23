def matriz16():
    mtx = [0]
    mtx[0] = []
    elm = int(0)
    for i in range(0,4):
        mtx.append(0)
        aux = []
        for j in range(0,4):
            aux.append(elm)
            elm += 1
        mtx[i] = aux.copy()
    return mtx

m = matriz16()
for i in range(4):
    print(m[i])
