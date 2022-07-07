import numpy as np
import random
import funciones as f

# Tres tableros
tablero_vacio = np.full((10,10), fill_value=" ")
tablero_j = np.full((10,10), fill_value=" ")
tablero_m = np.full((10,10), fill_value=" ")

# Barcos con sus coordenadas
barco_4 = [(8,6), (8,7), (8,8), (8,9)]

barco_3_1 = [(0,1), (1,1), (2,1)]
barco_3_2 = [(2,6), (3,6), (4,6)]

barco_2_1 = [(6,0), (6,1)]
barco_2_2 = [(8,3), (9,3)]
barco_2_3= [(4,9), (5,9)]


barco_1_1 = [(1,8)]
barco_1_2 = [(4,3)]
barco_1_3 = [(1,4)]
barco_1_4 = [(9,0)]

# lista d barcos
lista_barcos = [barco_4, barco_3_1, barco_3_2, barco_2_1, barco_2_2, barco_2_3, barco_1_1, barco_1_2, barco_1_3, barco_1_4]

# tableros con barcos
tablero_j = colocar_barcos_j(tablero_j, lista_barcos)
tablero_m = colocar_barcos_m(tablero_m, lista_barcos)

# turnos de jugador y máquina
j = turno_jugador()
tablero_j, disparo_j=disparo_jugador(tablero_j,j)

m = turno_maquina()
tablero_m, disparo_m = disparo_maquina(tablero_m,m)