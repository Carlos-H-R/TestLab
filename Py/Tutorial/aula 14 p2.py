n = int(input("Digite o número de empresas: "))
m = int(input("Digite o número de meses: "))
i = 0
j = 0

while i < n:
    print("Empresa",i+1,":")
    balanca = 0
    while j < m:
        print("Mês",j+1)
        a = int(input("Insira o ganho da empresa no mês:"))
        b = int(input("Insira o gasto da empresa no mês:"))
        balanca = balanca + (a - b)
        j = j+1
    if balanca > 0:
            print("A empresa",i+1,"lucrou R$",balanca)
    elif balanca == 0:
            print("A empresa",i+1,"teve balanço indiferente")
    else:
            print("A empresa",i+1,"teve déficit de R$",balanca)
    i = i+1
    j = 0
    
