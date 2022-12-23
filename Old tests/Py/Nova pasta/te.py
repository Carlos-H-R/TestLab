salva = open('test.txt','w')
for i in range(0,4):
    nome = input()
    nota = input()
    salva.write(str(nome+' '+nota))
