def media(a):
    x = 0
    for i in a:
        x += float(i)
    m = x/(int(len(a)))
    return m

    
def entrada():
    a = True
    while a:
        at = str(input('\nAtleta: '))
        if at == '':
            break
        s1 = str(input('\nPrimeiro Salto: '))
        s2 = str(input('Segundo Salto: '))
        s3 = str(input('Terceiro Salto: '))
        s4 = str(input('Quarto Salto: '))
        s5 = str(input('Quinto Salto: '))
        salt = [s1,s2,s3,s4,s5]
        node = [at,salt]
        memo.append(node)

def ler(nome):
    v = 0
    for i in memo:
        if i[0] == nome:
            f = ' - '.join(i[1])
            m = media(i[1])
            print('\nResultado Final: \nAtleta: ',i[0])
            print('Saltos: ',f)
            print('Média dos saltos: %2.f m'%m)
            v = 1
    if v != 1:
        print('Nome não encontrado!')


memo = []
entrada()

n = str(input('Qual nome deseja buscar? '))
ler(n)
