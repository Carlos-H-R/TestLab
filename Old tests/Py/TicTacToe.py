def cleantable(tab):
    tab = [[' ','|',' ','|',' '],
           ['-',' ','-',' ','-'],
           [' ','|',' ','|',' '],
           ['-',' ','-',' ','-'],
           [' ','|',' ','|',' ']]
    return tab
    

def iniciar():
    p1 = str(input("Jogador 1: "))
    p2 = str(input("Jogador 2: "))
    print("Cada espaço do tabuleiro está associado\n"
          "a um número (de 1 a 9).\n")
    return p1,p2
