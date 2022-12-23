def test_year(x):
    return x % 4 == 0 and (x %400 == 0 or x % 100 != 0)

def printer(t,y):
    if t == True:
        print("%i is a leap year"%y)
        print("")
    else:
        print("%i is not a leap year"%y)
        print("")

def entry():
    print("")
    lock = True
    while lock == True:
        y = input("Insert the year to be verified: ")
        print("")

        if y.isdigit() == True and y.isdecimal() == True:
            year = int(y)
            if 1900 <= year <= 10**5:
                lock = False
            else:
                ("Out of the defined range")

        else:
            print("Invalid Entry!")
            print("")
    return year

key = True
while key == True:
    x = entry()
    a = test_year(x)
    printer(a,x)
    

    b = input("Want to continue? ")
    b = b.upper()
    print("")

    if b == 'YES':
        print("")

    elif b == 'NO' or b == 'NOT':
        print("Task Finished!")
        print("")
        input("Press ENTER to close")
        key = False

    else:
        print("Invalid Entry!")
        print("")
    
        
