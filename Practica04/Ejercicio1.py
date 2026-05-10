# CLASE PAGINA (COMPOSICION)
class Pagina:
    def __init__(self, numero_pagina, contenido):
        self.__numero_pagina = numero_pagina
        self.__contenido = contenido

    def get_numero_pagina(self):
        return self.__numero_pagina

    def set_numero_pagina(self, numero):
        self.__numero_pagina = numero

    def get_contenido(self):
        return self.__contenido

    def set_contenido(self, contenido):
        self.__contenido = contenido

    def mostrar_pagina(self):
        print(f"Pagina {self.__numero_pagina}: {self.__contenido}")


# CLASE HORARIO (COMPOSICION)
class Horario:
    def __init__(self, dias_apertura, hora_apertura, hora_cierre):
        self.__dias_apertura = dias_apertura
        self.__hora_apertura = hora_apertura
        self.__hora_cierre = hora_cierre

    def get_dias_apertura(self):
        return self.__dias_apertura

    def set_dias_apertura(self, dias):
        self.__dias_apertura = dias

    def get_hora_apertura(self):
        return self.__hora_apertura

    def set_hora_apertura(self, hora):
        self.__hora_apertura = hora

    def get_hora_cierre(self):
        return self.__hora_cierre

    def set_hora_cierre(self, hora):
        self.__hora_cierre = hora

    def mostrar_horario(self):
        print("Horario de atencion")
        print("Dias:", self.__dias_apertura)
        print("Hora apertura:", self.__hora_apertura)
        print("Hora cierre:", self.__hora_cierre)


# CLASE LIBRO (AGREGACION)
class Libro:
    def __init__(self, titulo, isbn, paginas):
        self.__titulo = titulo
        self.__isbn = isbn

        # COMPOSICION
        self.__paginas = []

        for i, contenido in enumerate(paginas, start=1):
            pagina = Pagina(i, contenido)
            self.__paginas.append(pagina)

    def get_titulo(self):
        return self.__titulo

    def set_titulo(self, titulo):
        self.__titulo = titulo

    def get_isbn(self):
        return self.__isbn

    def set_isbn(self, isbn):
        self.__isbn = isbn

    def get_paginas(self):
        return self.__paginas

    def leer(self):
        print(f"\nLeyendo libro: {self.__titulo}")

        for pagina in self.__paginas:
            pagina.mostrar_pagina()


# CLASE AUTOR (AGREGACION)
class Autor:
    def __init__(self, nombre, nacionalidad):
        self.__nombre = nombre
        self.__nacionalidad = nacionalidad

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_nacionalidad(self):
        return self.__nacionalidad

    def set_nacionalidad(self, nacionalidad):
        self.__nacionalidad = nacionalidad

    def mostrar_info(self):
        print("Autor:", self.__nombre)
        print("Nacionalidad:", self.__nacionalidad)


# CLASE ESTUDIANTE (ASOCIACION)
class Estudiante:
    def __init__(self, codigo, nombre):
        self.__codigo = codigo
        self.__nombre = nombre

    def get_codigo(self):
        return self.__codigo

    def set_codigo(self, codigo):
        self.__codigo = codigo

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def mostrar_info(self):
        print("Codigo:", self.__codigo)
        print("Nombre:", self.__nombre)


# CLASE PRESTAMO (ASOCIACION)
class Prestamo:
    def __init__(self, estudiante, libro, fecha_prestamo, fecha_devolucion):
        self.__estudiante = estudiante
        self.__libro = libro
        self.__fecha_prestamo = fecha_prestamo
        self.__fecha_devolucion = fecha_devolucion

    def get_estudiante(self):
        return self.__estudiante

    def get_libro(self):
        return self.__libro

    def mostrar_info(self):
        print("\n===== PRESTAMO =====")
        print("Estudiante:", self.__estudiante.get_nombre())
        print("Libro:", self.__libro.get_titulo())
        print("Fecha prestamo:", self.__fecha_prestamo)
        print("Fecha devolucion:", self.__fecha_devolucion)


# CLASE BIBLIOTECA
class Biblioteca:
    def __init__(self, nombre, dias, apertura, cierre):
        self.__nombre = nombre

        # AGREGACION
        self.__libros = []
        self.__autores = []

        # ASOCIACION
        self.__prestamos = []

        # COMPOSICION
        self.__horario = Horario(dias, apertura, cierre)

    def get_nombre(self):
        return self.__nombre

    def agregar_libro(self, libro):
        self.__libros.append(libro)
        print(f"Libro '{libro.get_titulo()}' agregado.")

    def agregar_autor(self, autor):
        self.__autores.append(autor)
        print(f"Autor '{autor.get_nombre()}' registrado.")

    def prestar_libro(self, estudiante, libro):
        prestamo = Prestamo(
            estudiante,
            libro,
            "10/05/2026",
            "17/05/2026"
        )

        self.__prestamos.append(prestamo)

        print(f"Libro '{libro.get_titulo()}' prestado a {estudiante.get_nombre()}.")

    def mostrar_estado(self):
        print("\n==============================")
        print("BIBLIOTECA:", self.__nombre)
        print("==============================")

        print("\n--- HORARIO ---")
        self.__horario.mostrar_horario()

        print("\n--- LIBROS ---")
        for libro in self.__libros:
            print("-", libro.get_titulo())

        print("\n--- AUTORES ---")
        for autor in self.__autores:
            print("-", autor.get_nombre())

        print("\n--- PRESTAMOS ---")
        for prestamo in self.__prestamos:
            prestamo.mostrar_info()

    def cerrar_biblioteca(self):
        print("\nLa biblioteca ha sido cerrada.")
        self.__prestamos.clear()
        print("Los prestamos dejaron de existir.")


# MAIN

# COMPOSICION LIBRO-PAGINA
contenido_paginas = [
    "Introducción a Python",
    "Variables y tipos de datos",
    "POO en Python"
]

libro1 = Libro(
    "Python Basico",
    "ISBN-12345",
    contenido_paginas
)

# AGREGACION
autor1 = Autor("Gabriel Garcia Marquez", "Colombiano")

# ASOCIACION
estudiante1 = Estudiante("2024001", "Juan Perez")

# BIBLIOTECA
biblioteca = Biblioteca(
    "Biblioteca Central UMSA",
    "Lunes a Viernes",
    "08:00",
    "20:00"
)

# AGREGAR LIBRO Y AUTOR
biblioteca.agregar_libro(libro1)
biblioteca.agregar_autor(autor1)

# LEER LIBRO
libro1.leer()

# PRESTAR LIBRO
biblioteca.prestar_libro(estudiante1, libro1)

# MOSTRAR ESTADO
biblioteca.mostrar_estado()

# CERRAR BIBLIOTECA
biblioteca.cerrar_biblioteca()