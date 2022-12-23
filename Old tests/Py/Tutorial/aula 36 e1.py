def registrar(r):
    global log

    log.append(0)
    n = (len(log)-1)
    log[n] = [0]*3
    log[n][0] = r
    log[n][1] = input("Digite o nome do cliente: ")
    log[n][2] = input("Digite o valor a ser depositado: ")

    print("Dados registrados com sucesso!\n")
    return n
    
def buscar(r):
    global log
    
    ok = -1
    for i in range(len(log)):
        if r == log[i][0]:
            print("Número do Cliente: ",log[i][0])
            print("Nome do Cliente: ",log[i][1])
            print("Saldo do Cliente: ",log[i][2])
            linha = i
            ok = 1
    if ok == -1:
        print("\nRegistro não encontrado!\n")
        linha = -1
    return linha

def editar(ln):
    global log

    key = True
    while key:
        x = int(input("\n1 - editar o nome \n2 - editar o saldo \n3 - finalizar alterações\n--> "))

        if x == 1:
            log[ln][1] = input("Digite o novo nome: ")
        elif x == 2:
            log[ln][2] = float(input("Digite o novo saldo: "))
        elif x == 3:
            key = False
        else:
            print("\nEntrada Inválida!\n")

    print("\nRegistro atualizado\n")
    print("Número do Cliente:",log[ln][0])
    print("Nome do Cliente:",log[ln][1])
    print("Saldo do Cliente: R$%.2f"%(float(log[ln][2])))

def menu():
    k = True
    while k:
        r = input("\nInsira o número do cliente: ")
        if r.isdigit():
            if len(r) == 6:
                k = False
            else:
                print("\nO número do cliente deve conter 6 dígitos")

        else:
            print("\nEntrada Inválida!")
    return int(r)

log = [0]
log[0] = [0]*3
print("Bem Vindo ao banco PY")

lock = True
while lock:
    print("\nMENU\n\nPara prosseguir pressione (1)\nPara encerrar o programa pressione(0)")
    y = input("--> ")

    if y.isdigit():
        y = int(y)
        if y == 1:
            r = [menu()]
            a = buscar(r)
            if a == -1:
                n = registrar(r)
                editar(n)
            else:
                editar(a)
        elif y == 0:
            lock = False
            print("\nPROGRAMA ENCERRADO!\n")
            input("Pressione ENTER fechar")
        else:
            print("Comando Inválido!")
    else:
        print("Comando Inválido!")

    
