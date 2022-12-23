def tab(a):
    base = a
    def num():
        nonlocal base
        multi = 1
        for i in range(10):
            result = base * multi
            print("%i * %i = %i"%(base,multi,result))
            multi += 1
    return num()

n = int(input("Digite um número: "))

for i in range(n):
    print("Tabuáda do número %i"%(i+1))
    tab(i+1)
    print("")
