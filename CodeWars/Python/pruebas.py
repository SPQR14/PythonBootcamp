tablero = [['1 ', '| ', '2 ', '| ', '3'],
           ['- ','- ' ,'- ', '- ' ,'- '], 
           ['4 ', '| ', '5 ', '| ', '6'],
           ['- ','- ' ,'- ', '- ' ,'- '], 
           ['7 ', '| ', '8 ', '| ', '9']]
jugador = 1
turno = 2
print(f"turno del jugador: {jugador}",end='')
print(f"\t\tturno {turno}, restantes {9-turno}", end='')
print("\n\n\n")
for i in range(0, 5):
    for j in range(0, 5):
        print(tablero[i][j], end='')
    print()

entrada = int(input("tirale mamada"))