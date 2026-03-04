import time

class Cronometro:

    def __init__(self):
        self.__inicia = time.time()
        self.__finaliza = None

    def inicia(self):
        self.__inicia = time.time()

    def detener(self):
        self.__finaliza = time.time()

    def lapsoDeTiempo(self):
        return (self.__finaliza - self.__inicia) * 1000  # milisegundos

    def getInicia(self):
        return self.__inicia

    def getFinaliza(self):
        return self.__finaliza

import random

numeros = [random.randint(1, 10000) for _ in range(10000)]

crono = Cronometro()

crono.inicia()

for i in range(len(numeros)):
    min_index = i
    for j in range(i+1, len(numeros)):
        if numeros[j] < numeros[min_index]:
            min_index = j
    numeros[i], numeros[min_index] = numeros[min_index], numeros[i]

crono.detener()

print("Tiempo transcurrido en milisegundos:", crono.lapsoDeTiempo())