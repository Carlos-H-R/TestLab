saque = int(input("Insira o valor do saque:"))
n100 = saque//100
n50 = (saque%100)//50
n10 = ((saque%100)%50)//10
n5 = (((saque%100)%50)%10)//5
n1 = (((saque%100)%50)%10)%5
if 10 <= saque <= 600:
    print("Para sacar",saque,"reais, serão emitidas:")
    if n100 != 0:
        print(n100,"notas de 100")
    if n50 != 0:
        print(n50,"notas de 50")
    if n10 != 0:
        print(n10,"notas de 10")
    if n5 != 0:
        print(n5,"notas de 5")
    if n1 != 0:
        print(n1,"notas de 1")
else:
    print("Valor inválido!")
    
    
