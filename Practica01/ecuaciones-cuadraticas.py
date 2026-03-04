import math

class EcuacionCuadratica:

    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def getDiscriminante(self):
        return self.__b**2 - 4*self.__a*self.__c

    def getRaiz1(self):
        d = self.getDiscriminante()
        if d >= 0:
            return (-self.__b + math.sqrt(d)) / (2*self.__a)
        else:
            return 0

    def getRaiz2(self):
        d = self.getDiscriminante()
        if d >= 0:
            return (-self.__b - math.sqrt(d)) / (2*self.__a)
        else:
            return 0
a, b, c = map(float, input("Ingrese a, b, c: ").split())

ecuacion = EcuacionCuadratica(a, b, c)

d = ecuacion.getDiscriminante()

if d > 0:
    print("La ecuacion tiene dos raices",
        ecuacion.getRaiz1(),
        "y",
        ecuacion.getRaiz2())
elif d == 0:
    print("La ecuacion tiene una raiz",
        ecuacion.getRaiz1())
else:
    print("La ecuacion no tiene raices reales")