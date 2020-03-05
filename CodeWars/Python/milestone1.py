"""
Milestone
"""


import os

tablero = [['1 ', '| ', '2 ', '| ', '3'],
           ['- ','- ' ,'- ', '- ' ,'- '], 
           ['4 ', '| ', '5 ', '| ', '6'],
           ['- ','- ' ,'- ', '- ' ,'- '], 
           ['7 ', '| ', '8 ', '| ', '9']]

jugadas = {1: [[0][0]], 2: [[0][2]], 3: [[0][4]], 
           4: [[2][0]], 5: [[2][2]], 6: [[2][4]],
           7: [[4][0]], 8: [[4][0]], 9: [[4][0]]}

tiradas = []
jugador1 = []
jugador2 = []
turno = 1
jugador = 0

def inputs(message, tiradas):
    print("en este monento:")
    print(tiradas)
    while(True):
        entrada = int(input(message))
        if (entrada >= 1 and entrada <= 9):
            if entrada in tiradas:
                print("Wrong movement, try again!")
            else:
                return entrada
        else:
            print("Must be a number between 1 and 9")


def imprimir_tablero():
    print(f"turno del jugador: {jugador}",end='')
    print(f"\t\tturno {turno}, restantes {9-turno}\n\n")
    for x in range(5):
        for y in range(5):
            print(tablero[x][y], end='')
        print()


def actualiza_tablero(tiro):
    tiro = str(tiro)
    for item in jugadas:
        if item == tiro:
            pass           


while(True):
    os.system("cls")
    a = inputs("which grad?: ", tiradas)
    tiradas.append(a)
    imprimir_tablero()
    os.system("pause")
   
    

   