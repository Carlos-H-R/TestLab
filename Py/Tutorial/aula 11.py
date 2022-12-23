num = int(input("Digite um número:"))

if 100 <= num < 1000:
    print(num//100,"centenas,",((num%100)//10),"dezenas,",((num%100)%10),"unidades.")
elif 10 <= num < 100:
    print(num//10,"dezenas,",num%10,"unidades.")
elif num < 10:
    print(num,"unidades.")
else:
    print("Valor inválido! Digite um número menor que 1000.")
