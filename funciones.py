# tablero = inicializa_tablero()

# tablero = colocar_barcos(tablero, lista_barcos)

# tablero = disparo(tablero, (3,4))

# print(tablero)

# para colocar barcos de jugador:
def colocar_barco_j(tablero_j, barco):
    for elem in barco:
        print("Colocando barco en posicion", elem)
        tablero_j[elem] = "O"
    return tablero_j

def colocar_barcos_j(tablero_j, barcos):
    for barco in barcos:
        tablero_j = colocar_barco_j(tablero_j, barco)
    return tablero_j

# para colocar barcos de máquina:
def colocar_barco_m(tablero_m, barco):
    for elem in barco:
        print("Colocando barco en posicion", elem)
        tablero_m[elem] = "O"
    return tablero_m

def colocar_barcos_m(tablero_m, barcos):
    for barco in barcos:
        tablero_m = colocar_barco_m(tablero_m, barco)
    return tablero_m

# turno y disparo de jugador
def turno_jugador():
    row = int(input('Row: ')) -1
    col = int(input('Col: ')) -1
    return (row, col)
    

def disparo_jugador(tablero_j, turno_jugador):
    if tablero_j[turno_jugador] == "O":
        print("Tocado")
        tablero_j[turno_jugador] = "X"
        disparo = 'Tocado'
    else:
        print("Agua")
        tablero_j[turno_jugador] = "A"
        disparo = 'Agua'
    
    return tablero_j, disparo

# turno y disparo de máquina
def turno_maquina():
    # Subtract 1 to adjust for python 0-based indexing
    row = np.random.randint(10)
    col = np.random.randint(10)
    return (row, col)
    

def disparo_maquina(tablero_m, turno_maquina):
    if tablero_m[turno_maquina] == "O":
        print("Tocado")
        tablero_m[turno_maquina] = "X"
        disparo = 'Tocado'
    else:
        print("Agua")
        tablero_m[turno_maquina] = "A"
        disparo = 'Agua'
    
    return tablero_m, disparo


