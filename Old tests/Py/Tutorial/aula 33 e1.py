def imposto(t,c):
    nc = (1+(t/100)) * c
    return nc

t = float(input("Digite a porcentagem de imposto: "))
c = float(input("Digite o custo do produto: "))

print("O custo ajustado do produto é R$ %.2f"%(imposto(t,c)))
