import matplotlib.pyplot as plt
import numpy as np

ciudades = ["Nueva York", "Rio de Janeiro", "Tokyo"]
posiciones = [[3, 20], [3, 5], [60, 30], [10, 11], [45, 5]]
indice = [0, 1, 2]
viajes = []
distancias = [
    10,
    22,
    68
]


def imprime_variantes(indice):
    contador = 0
    for i in indice:
        indice[contador] = ciudades[contador]
        contador += 1
    # -----------------------------------------------------------

    def swap(lst, a, b):
        lst[a], lst[b] = lst[b], lst[a]

    def permutar(indice, ultimo_numero, ultima_posible):
        if ultimo_numero == ultima_posible:
            print(indice)

        else:
            for numero_actual in range(ultimo_numero, ultima_posible + 1):
                swap(indice, numero_actual, ultimo_numero)
                permutar(indice, ultimo_numero + 1, ultima_posible)
                swap(indice, numero_actual, ultimo_numero)

    n = len(indice)
    l = indice
    permutar(l, 0, n-1)
    return indice


def imprime_distancias(buffer, distancias):

    i = 0
    max = len(distancias)
    while i < max:
        buffer[i] += f'distancia[{distancias[i]}]'

    return buffer


print(imprime_variantes(indice))
