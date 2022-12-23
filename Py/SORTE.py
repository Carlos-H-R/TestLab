#Created by: Mr.Charlie

import random
master = True

while master == True:
    print("")
    print("Defina o intervalo para jogar")
    i = int(input("Insira o início do intervalo: "))
    f = int(input("Insira o fim do intervalo: "))

    x = random.randint(i,f)

    lock = True
    while lock == True:
        print("")
        j = input("Tente advinhar o número sorteado: ")
        print("")

        if j.isdigit() == True:
            k = int(j)

            if i <= k <= f:

                if k == x:
                    print("Parabéns! Você acertou!")
                    print("O número sorteado foi %i"%x)
                    print("")
                    lock = False
                    key = False
                    while key == False:
                        q = input("Deseja jogar novamente? --> ")
                        qq = q.upper()
                        
                        if qq == 'SIM':
                            key = True
                        elif qq == 'NAO' or qq == 'NÃO':
                            print("")
                            print("Programa encerrado!")
                            input("Pressione ENTER para fechar")
                            master = False
                            key = True
                        else:
                            print("")
                            print("Entrada inválida!")
                            print("")
                            

                else:
                    print("Você errou! Tente novamente")
                
            else:
                print("Fora do intervalo!")

        else:
            print("Entrada Inválida!")
