lock = False
while lock == False:
        newsal = 0
        print("")
        oldsal = float(input("Insira o salário: "))
        if 0 < oldsal <= 280:
            newsal = oldsal * 1.2
            print("O salário antes do reajuste é R$ %4.2f"%oldsal)
            print("O percentual de aumento aplicado é de 20%")
            print("O aumento foi de R$ %4.2f"%(newsal-oldsal))
            print("O novo salário é de R$ %4.2f"%newsal)
        elif 280 < oldsal <= 700:
            newsal = oldsal * 1.15
            print("O salário antes do reajuste é R$ %4.2f"%oldsal)
            print("O percentual de aumento aplicado é de 15%")
            print("O aumento foi de R$ %4.2f"%(newsal-oldsal))
            print("O novo salário é de R$ %4.2f"%newsal)
        elif 700 < oldsal <= 1500:
            newsal = oldsal * 1.1
            print("O salário antes do reajuste é R$ %4.2f"%oldsal)
            print("O percentual de aumento aplicado é de 10%")
            print("O aumento foi de R$ %4.2f"%(newsal-oldsal))
            print("O novo salário é de R$ %4.2f"%newsal)
        elif oldsal > 1500:
            newsal = oldsal * 1.05
            print("O salário antes do reajuste é R$ %4.2f"%oldsal)
            print("O percentual de aumento aplicado é de 5%")
            print("O aumento foi de R$ %4.2f"%(newsal-oldsal))
            print("O novo salário é de R$ %4.2f"%newsal)
        elif oldsal == 0:
            lock = True
        else:
            print("Entrada Inválida")
            
