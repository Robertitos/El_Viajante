import matplotlib.pyplot as plt
import numpy as np

ciudades = ["Nueva York", "Rio de Janeiro", "Tokyo"]
posiciones = [[3, 20], [3, 5], [60, 30], [10, 11], [45, 5]]
indice = [0, 1, 2]
viajes = []
distancias = [
    10,
    22,
    68,
    10,
    22,
    68    
]

def imprime_variantes(indice):
    def swap(lst, a, b):
        lst[a], lst[b] = lst[b], lst[a]

    def permutar(indice, ultimo_numero, ultima_posible):
        if ultimo_numero == ultima_posible:
            viajes.append(indice.copy())
        else:
            for numero_actual in range(ultimo_numero, ultima_posible + 1):
                swap(indice, numero_actual, ultimo_numero)
                permutar(indice, ultimo_numero + 1, ultima_posible)
                swap(indice, numero_actual, ultimo_numero)

    permutar(indice, 0, len(indice) - 1)

def imprime_viajes(ciudades, viajes):
    buffer = []
    for viaje in viajes:
        buffer_linea = ""
        for indice in viaje:
            buffer_linea += ' >> ' + ciudades[indice] 
        buffer.append(buffer_linea)

    return buffer

def imprime_distancias(buffer, distancias):
    if(len(buffer) != len(distancias)):
        exit("ERROR: las distanciasn mnas,dnas,dna,s")
    
    contador = 0
    while contador <= len(buffer) - 1:
        buffer[contador] += f"  DIST: [{distancias[contador]}] unidades"
        contador += 1
    
    return buffer
        
    

    

imprime_variantes(indice)
buffer = imprime_viajes(ciudades, viajes)
buffer = imprime_distancias(buffer, distancias)



for linea in buffer:
    print(linea)
