lock = True

while lock == True:
    y = input("Insira o ano a ser verificado: ")

    if y.isdigit() == True and y.isdecimal() == True:
        year = int(y)
        lock = False

    else:
        print("Entrada Inválida!")

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 ==0:
            test = True

        else:
            test = False

    else:
        test = True

else:
    test = False

if test == True:
    print("%i is a leap year")

else:
    print("%i is not a leap year"%year)
