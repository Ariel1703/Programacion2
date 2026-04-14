import random

class Juego:
    def __init__(self, numeroDeVidas):
        self.numeroDeVidas = numeroDeVidas
        self.record = 0

    def reiniciaPartida(self):
        print("Nueva partida iniciada")
    
    def actualizaRecord(self):
        self.record += 1
        print("Record actualizado:", self.record)

    def quitaVida(self):
        self.numeroDeVidas -= 1
        if self.numeroDeVidas > 0:
            return True
        else:
            print("Game Over")
            return False

class JuegoAdivinaNumero(Juego):
    def __init__(self, vidas):
        super().__init__(vidas)
        self.numeroAdivinar = 0

    def juega(self):
        self.reiniciaPartida()
        self.numeroAdivinar = random.randint(0, 10)

        while True:
            num = int(input("Adivina un número (0-10): "))

            if num == self.numeroAdivinar:
                print("¡Acertaste!")
                self.actualizaRecord()
                break
            else:
                if self.quitaVida():
                    if num < self.numeroAdivinar:
                        print("El numero es mayor")
                    else:
                        print("El numero es menor")
                else:
                    break

class JuegoAdivinaPar(JuegoAdivinaNumero):

    def validaNumero(self, num):
        if num % 2 != 0:
            print("Error: debe ser número PAR")
            return False
        return 0 <= num <= 10

class JuegoAdivinaImpar(JuegoAdivinaNumero):

    def validaNumero(self, num):
        if num % 2 == 0:
            print("Error: debe ser número IMPAR")
            return False
        return 0 <= num <= 10

if __name__ == "__main__":
    print("=== Juego normal ===")
    j1 = JuegoAdivinaNumero(3)
    j1.juega()

    print("\n=== Juego PAR ===")
    j2 = JuegoAdivinaPar(3)
    j2.juega()

    print("\n=== Juego IMPAR ===")
    j3 = JuegoAdivinaImpar(3)
    j3.juega()