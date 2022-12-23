area = float(input('Insira a área a ser pintada: '))
vlata = 80.00
vgalao = 25.00
litro = 1.1*(area/6)
solata = 0
sogalao = 0
misto = 0

misto = ((litro//18)*vlata)+((litro%18)*vgalao)
if litro%18 == 0:
    solata = vlata*(litro//18)
else:
    solata = vlata*((litro//18)+1)
if litro%4 == 0:
    sogalao = vgalao*(litro//4)
else:
    sogalao = vgalao*((litro//4)+1)


print('A quantidade de tinta necessária é',litro,'litros.')
print('Se comprar apenas latas de 18L custará:',solata)
print('se comprar apelas galões de 4L custará:',sogalao)
print('Se comprar uma mistura de latas e galões custará:',misto)
