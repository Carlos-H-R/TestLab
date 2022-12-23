m = [0]*5
for i in range(5):
    m[i] = [input('Nome: '),int(input('Idade: '))]
print(*m)

age = m[0][1]
for k in m:
    if k[1] <= age:
        age = k[1]
        quem = k[0]

print('O(A) mais novo(a) é %s com %i ano de idade'%(quem,age))
    
