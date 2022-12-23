def comparadorX(n):
    tempx = n[0]
    for i in range(1,len(n)):
        if int(n[i]) >= int(tempx) :
            tempx = int(n[i])
    print("Temperatura máxima:")
    print(tempx)

def comparadorN(n):
    tempx = n[0]
    for i in range(0,len(n)):
        if int(n[i]) <= int(tempx) :
            tempx = int(n[i])
    print("Temperatura mínima:")
    print(tempx)
    
def mediador(n):
    soma = 0
    for i in range(0,len(n)):
        soma += n[i]
    media = soma/(len(n))
    print("Média das temperaturas:")
    print(media)

def lista(t):
    for i in range(0,t):
        ltemp[i] = float(input("Digite a temperatura:"))
    print("Lista de temperaturas")
    print(ltemp)
    return(ltemp)

k = int(input("Número de temperaruras: "))
ltemp = [0]*k
print("")
lista(k)
print("")
comparadorX(ltemp)
print("")
comparadorN(ltemp)
print("")
mediador(ltemp)
