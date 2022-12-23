memo = []
par = []
impar = []

print("Digite números inteiros")
for i in range(0,20):
    memo.append(int(input("#%i: "%(i+1))))

for i in range(0,20):
    x = memo[i]
    if x%2 == 0:
        par.append(x)

    else:
        impar.append(x)
        
print("Lista de elementos: ",memo)
print("")
print("Pares: ",par)
print("")
print("Impaes: ",impar)
   
