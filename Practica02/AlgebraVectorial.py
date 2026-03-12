import math

class AlgebraVectorial:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def producto_punto(self, v):
        return self.x*v.x + self.y*v.y

    def magnitud(self):
        return math.sqrt(self.x**2 + self.y**2)

    def perpendicular(self, v):
        return self.producto_punto(v) == 0

    def paralela(self, v):
        return (self.x * v.y - self.y * v.x) == 0

    def proyeccion(self, v):
        escalar = self.producto_punto(v) / (v.magnitud()**2)
        return (escalar*v.x, escalar*v.y)

    def componente(self, v):
        return self.producto_punto(v) / v.magnitud()


v1 = AlgebraVectorial(6,4)
v2 = AlgebraVectorial(8,-3)

print("Perpendiculares:", v1.perpendicular(v2))
print("Paralelos:", v1.paralela(v2))
print("Proyección:", v1.proyeccion(v2))
print("Componente:", v1.componente(v2))