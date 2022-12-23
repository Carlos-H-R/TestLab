#Created  by: Mr.Charlie
import random
lock = True

while lock == True:
    print("")
    y = input("Você gostaria de jogar o dado? ")
    x = y.upper()
    print("")

    if x == 'NÃO' or x == 'NAO':
        print("Programa Encerrado!")
        print("")
        input("Pressione ENTER para fechar")
        lock = False
        

    elif x == 'SIM':
        d = random.randint(1,6)
        print("O valor tirado no dado é %i"%d)

    else:
        print("Entrada Inválida!")
        
