lock = True

x = int(input("Digite um número: "))
vet = [x]

while lock == True:
    y = int(input("Digite outro número: "))
    if y == -1:
        lock = False

    else:
        vet.append(y)
print("")

key = True
while key == True:
    z = int(input("Insira qual número deseja contar: "))

    count = 0
    for i in range(0,len(vet)):
        if vet[i] == z:
            count += 1

    print("")
    print("O número %i apareceu %i vezes"%(z,count))
    print("")

    safe = True
    while safe == True:
        q = input("Deseja contar outro número? ")
        q = q.upper()

        if q == 'SIM':
            safe = False
            print("")

        elif q == 'NAO' or q == 'NÃO':
            safe = False
            key = False
            print("Programa Encerrado!")
            print("")
            input("Pressione ENTER para fechar")

        else:
            print("Entrada Inválida!")
