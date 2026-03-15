import math

class PoligonoRegular:

    def __init__(self, *args):

        # constructor sin argumentos
        if len(args) == 0:
            self.n = 3
            self.lado = 1
            self.x = 0
            self.y = 0

        # constructor con n y lado
        elif len(args) == 2:
            self.n = args[0]
            self.lado = args[1]
            self.x = 0
            self.y = 0

        # constructor con todos los valores
        elif len(args) == 4:
            self.n = args[0]
            self.lado = args[1]
            self.x = args[2]
            self.y = args[3]

    def getPerimetro(self):
        return self.n * self.lado

    def getArea(self):
        return (self.n * self.lado**2) / (4 * math.tan(math.pi / self.n))


# programa de prueba
p1 = PoligonoRegular()
p2 = PoligonoRegular(6, 4)
p3 = PoligonoRegular(10, 4, 5.6, 7.8)

print("Poligono 1")
print("Perimetro:", p1.getPerimetro())
print("Area:", p1.getArea())

print("\nPoligono 2")
print("Perimetro:", p2.getPerimetro())
print("Area:", p2.getArea())

print("\nPoligono 3")
print("Perimetro:", p3.getPerimetro())
print("Area:", p3.getArea())
