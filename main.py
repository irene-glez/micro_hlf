import funciones as f
import variables as v

# tablero = f.inicializar_tablero
# lista_barcos = [f.barco_aleatorio(2), f.barcoaleatorio(4)]
# tablero = f.colocar_barcos(tablero, lista_barcos)
# tablero 
# print(tablero)

print('¡Hola! Vas a jugar a \'Hundir la flota!\' en un tablero de 10 x 10 como este:')
print(tablero_vacio)
print('Ingresa las coordenadas para disparar (fila -> enter, columna -> enter).')

# para colocar barcos de jugador:
tablero_j = f.colocar_barcos_j(tablero_j, lista_barcos)

# para colocar barcos de máquina:
tablero_m = f.colocar_barcos_m(tablero_m, lista_barcos)


# turno y disparo de jugador:
tablero_j, disparo_j = disparo_jugador(tablero_j,j)

# turno y disparo de máquina:
tablero_m, disparo_m = disparo_maquina(tablero_m,m)

# W H I L E para empezar a jugar

disparo_j = ''
disparo_m = ''

while 'O' in tablero_j and 'O' in tablero_m:
    while disparo_j != 'Agua':
        j = turno_jugador()
        print('Has dado en:')
        tablero_m, disparo_j = disparo_jugador(tablero_m, j)
        print(tablero_m)
        
    while disparo_m != 'Agua':
        m = turno_maquina()
        print('Bender ha dado en:')
        tablero_j, disparo_m = disparo_maquina(tablero_j, m)
        print(tablero_j)

    disparo_j = ''
    disparo_m = ''