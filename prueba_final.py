import matplotlib.pyplot as plt
import numpy as np

ciudades = ["Nueva York", "Rio de Janeiro", "Tokyo"]
posiciones = [[3,20], [3,5], [60,30], [10,11], [45,5]]
indice =[0, 1, 2]
viajes = []

def imprime_variantes(indice):
    contador = 0
    for i in indice:
        indice[contador] = ciudades[contador]
        contador += 1
    #-----------------------------------------------------------
    def swap(lst, a, b):
        lst[a], lst[b] = lst[b], lst[a]

    def permutar(indice, ultimo_numero, ultima_posible):
        if ultimo_numero == ultima_posible:

            print(indice)       

        else:
            for numero_actual in range(ultimo_numero, ultima_posible + 1):
                #ciudades[ultimo_numero], ciudades[numero_actual] = ciudades[numero_actual], ciudades[ultimo_numero]
                swap(indice, numero_actual, ultimo_numero)

                permutar(indice, ultimo_numero + 1, ultima_posible)

                # ciudades[ultimo_numero], ciudades[numero_actual] = ciudades[numero_actual], ciudades[ultimo_numero]
                swap(indice, numero_actual, ultimo_numero)
            



    n = len(indice)
    l = indice

    permutar(l, 0, n-1)

    return indice

distancias = [
    10, 
    22, 
    68
    ]

"""def imprime_viajes(ciudades, indice):
    buffer = []
    for viaje in viajes:
        buffer_linea = ""
        for indice in viaje:
            buffer_linea += ' >> ' + ciudades[indice] 
        buffer.append(buffer_linea)

    return buffer"""

def imprime_distancias(buffer, distancias):
    
    i = 0
    max = len(distancias)
    while i < max:
        buffer[i] += f'distancia[{distancias[i]}]'

    return buffer

"""def dibuja_mapa(posiciones):
    def dibuja_ciudades(posiciones):
        contador = 0

        while contador < len(ciudades):
            x = np.array(ciudades[contador][0])
            y = np.array(ciudades[contador][1])
            contador += 1

            plt.scatter(x, y)
            plt.plot(ciudades[:, 0], ciudades[:, 1], color = "b")


plt.xlabel("X")
plt.ylabel("Y")
plt.show()"""

print(imprime_variantes(indice))





