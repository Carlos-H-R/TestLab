def entrada(l):
    print("Insira os números em sequência no campo entrada, para encerrar a lista digite '-1'")
    print("")

    x = 0
    while x != -1:
        x = int(input("Entrada: "))
        print("")

        if x != -1:
            l.append(x)

        else:
            print("Lista encerrada!")
            print("")
    return(l)

def consulta(l):
    print(l)

    c = int(input("Escolha um número para ser consultado: "))

    count = 0
    for i in range(0,len(l)):
        if c == l[i]:
            count += 1

    print("")
    print("O número %i aparece %i vezes na lista"%(c,count))

l=[]
entrada(l)
consulta(l)
