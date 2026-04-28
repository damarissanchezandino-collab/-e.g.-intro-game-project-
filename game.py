def imprimir_tablero(tablero):
    for fila in tablero:
        print(" | ".join(fila))
        print("-" * 9)

def verificar_ganador(tablero, jugador):
    # Filas, columnas y diagonales
    for i in range(3):
        if all([s == jugador for s in tablero[i]]) or \
           all([tablero[j][i] == jugador for j in range(3)]):
            return True
    if tablero[0][0] == tablero[1][1] == tablero[2][2] == jugador or \
       tablero[0][2] == tablero[1][1] == tablero[2][0] == jugador:
        return True
    return False

def jugar():
    tablero = [[" " for _ in range(3)] for _ in range(3)]
    jugador_actual = "X"
    
    for turno in range(9):
        imprimir_tablero(tablero)
        print(f"Turno de {jugador_actual}")
        
        fila = int(input("Fila (0-2): "))
        col = int(input("Columna (0-2): "))
        
        if tablero[fila][col] == " ":
            tablero[fila][col] = jugador_actual
            if verificar_ganador(tablero, jugador_actual):
                imprimir_tablero(tablero)
                print(f"¡El jugador {jugador_actual} ha ganado!")
                return
            jugador_actual = "O" if jugador_actual == "X" else "X"
        else:
            print("Espacio ocupado, intenta de nuevo.")
            
    imprimir_tablero(tablero)
    print("¡Es un empate!")

jugar()
