from abc import ABC, abstractmethod
import random
#1. Convertir Juego en clase abstracta
class Juego(ABC):
    # Atributos
    def __init__(self, numeroDeVidas):
        self.numeroDeVidas = numeroDeVidas
        self.record = 0
    def reiniciaPartida(self):
        print("Nueva partida iniciada")
    def actualizaRecord(self):
        self.record += 1
        print("Record:", self.record)
    def quitaVida(self):
        self.numeroDeVidas -= 1
        if self.numeroDeVidas > 0:
            print("Te quedan", self.numeroDeVidas, "vidas")
            return True
        else:
            print("Game Over")
            return False
    # metodo abstracto obligatorio
    @abstractmethod
    def mostrarReglas(self):
        pass
#2 Crear la interfaz Jugable
class Jugable:
    # metodo para saludar al jugador
    def saludarJugador(self):
        pass
    # metodo para despedirse del jugador
    def despedidaJugador(self):
        pass
# Crear JuegoAdivinaNumero
class JuegoAdivinaNumero(Juego, Jugable):
    # Constructor
    def __init__(self, vidas):
        super().__init__(vidas)
        self.numeroAAdivinar = 0
    # metodo para validar que el numero este entre 0 y 10
    def validaNumero(self, n):
        return 0 <= n <= 10
    # Implementar metodo abstracto
    def mostrarReglas(self):
        print("Debes adivinar un numero entre 0 y 10")
    # Implementar metodo de la interfaz
    def saludarJugador(self):
        print("Bienvenido al juego")

    # Implementar metodo de la interfaz
    def despedidaJugador(self):
        print("Gracias por jugar")

    # metodo principal del juego
    def juega(self):
        self.saludarJugador()
        self.mostrarReglas()
        self.reiniciaPartida()
        self.numeroAAdivinar = random.randint(0, 10)
        while True:
            n = int(input("Ingrese un numero: "))
            if not self.validaNumero(n):
                print("Numero invalido")
                continue
            if n == self.numeroAAdivinar:
                print("Acertaste")
                self.actualizaRecord()
                break
            else:
                if self.quitaVida():
                    if n < self.numeroAAdivinar:
                        print("El numero es mayor")
                    else:
                        print("El numero es menor")
                else:
                    break
        self.despedidaJugador()
#3.Crear JuegoAdivinaPar
class JuegoAdivinaPar(JuegoAdivinaNumero):
    def __init__(self, vidas):
        super().__init__(vidas)
        self.disponibles = [0, 2, 4, 6, 8, 10]
    def mostrarReglas(self):
        print("Debes adivinar un numero PAR")
    def validaNumero(self, n):
        if n < 0 or n > 10:
            return False
        if n % 2 != 0:
            print("Error: debe ser par")
            return False
        return True
    def juega(self):
        self.saludarJugador()
        self.mostrarReglas()
        self.reiniciaPartida()
        self.numeroAAdivinar = random.choice([0, 2, 4, 6, 8, 10])
        while True:
            print("Disponibles:", self.disponibles)
            n = int(input("Ingrese un numero par: "))
            if not self.validaNumero(n):
                continue
            if n == self.numeroAAdivinar:
                print("Acertaste")
                self.actualizaRecord()
                break
            else:
                print("Incorrecto")
                if n in self.disponibles:
                    self.disponibles.remove(n)
                if not self.quitaVida():
                    break
        self.despedidaJugador()
#4.Crear JuegoAdivinaImpar
class JuegoAdivinaImpar(JuegoAdivinaNumero):
    def __init__(self, vidas):
        super().__init__(vidas)
        self.disponibles = [1, 3, 5, 7, 9]
    def mostrarReglas(self):
        print("Debes adivinar un numero IMPAR")
    def validaNumero(self, n):
        if n < 0 or n > 10:
            return False
        if n % 2 == 0:
            print("Error: debe ser impar")
            return False
        return True
    def juega(self):
        self.saludarJugador()
        self.mostrarReglas()
        self.reiniciaPartida()
        self.numeroAAdivinar = random.choice([1, 3, 5, 7, 9])
        while True:
            print("Disponibles:", self.disponibles)
            n = int(input("Ingrese un numero impar: "))
            if not self.validaNumero(n):
                continue
            if n == self.numeroAAdivinar:
                print("Acertaste")
                self.actualizaRecord()
                break
            else:
                print("Incorrecto")
                if n in self.disponibles:
                    self.disponibles.remove(n)
                if not self.quitaVida():
                    break
        self.despedidaJugador()
# main
j1 = JuegoAdivinaNumero(3)
j2 = JuegoAdivinaPar(3)
j3 = JuegoAdivinaImpar(3)

j1.juega()
j2.juega()
j3.juega()