def ajuste(oldsal):
    if 0 < oldsal <= 280:
            newsal = oldsal * 1.2
            print("O salário antes do reajuste é R$ %.2f"%oldsal)
            print("O percentual de aumento aplicado é de 20%")
            print("O aumento foi de R$ %.2f"%(newsal-oldsal))
            print("O novo salário é de R$ %.2f"%newsal)
            
    elif 280 < oldsal <= 700:
            newsal = oldsal * 1.15
            print("O salário antes do reajuste é R$ %.2f"%oldsal)
            print("O percentual de aumento aplicado é de 15%")
            print("O aumento foi de R$ %.2f"%(newsal-oldsal))
            print("O novo salário é de R$ %.2f"%newsal)
    elif 700 < oldsal <= 1500:
            newsal = oldsal * 1.1
            print("O salário antes do reajuste é R$ %.2f"%oldsal)
            print("O percentual de aumento aplicado é de 10%")
            print("O aumento foi de R$ %.2f"%(newsal-oldsal))
            print("O novo salário é de R$ %.2f"%newsal)
    elif oldsal > 1500:
            newsal = oldsal * 1.05
            print("O salário antes do reajuste é R$ %.2f"%oldsal)
            print("O percentual de aumento aplicado é de 5%")
            print("O aumento foi de R$ %.2f"%(newsal-oldsal))
            print("O novo salário é de R$ %.2f"%newsal)



def incluir():
    lock = False
    while lock == False:
        c = 5
        nomes.append(input("Insira o nome do funcionário: "))
        salarios.append(float(input("Insira o salário: ")))
        print("")
        h = 0
        while h == False:
            c = int(input("Digite '0' para retornar ao menu ou '1' para continuar: "))
            print("")
            if c == int(0):
                lock = True
                h = True
            elif c == int(1):
                h = True
            else:
                print("Comando Inválido!")
                h = False    
    return(nomes,salarios)


nomes = []
salarios = []
men = True
while men == True:
    print("MENU")
    print("")
    print("Digite:")
    print("1 - para inserir um novo salário")
    print("2 - para mostrar um salário específico")
    print("3 - para mostrar todos os salários")
    print("0 - para encerrar o programa")
    print("")
    x = int(input("-->"))
    print("")

    if x == 1:
        incluir()
        
        
    elif x == 2:
        pin = True
        while pin == True:
            s = int(input("Digite o número do item a ser resgatado: "))
            t = (s-1)
            print("")
            print("Funcionário: ",nomes[t])
            print("")
            ajuste(salarios[t])
            print("")
            pin = int(input("Digite '1' para continuar ou '0' para retornar ao menu: "))
        

    elif x == 3:
        for i in range(0,len(nomes)):
            print("Funcionário: ",nomes[i])
            print("")
            ajuste(salarios[i])
            print("")

    elif x == 0:
        print("Progema encerrado!")
        men = False
        

    else:
        print("Comando Inválido!")
        
            
