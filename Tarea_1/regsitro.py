#REGISTRO DE NOTAS

from datetime import date

class Asignatura:
    _secuencia = 0

    def __init__(self, nombre):
        Asignatura._secuencia += 1
        self.__id = Asignatura._secuencia
        self.nombre = nombre

    @property
    def id(self):
        return self.__id

    def mostrar(self):
        print("Asignatura:")
        print(f"ID: {self.id} - Nombre: {self.nombre}\n")

class Profesor:
    _secuencia = 0

    def __init__(self, nombre, apellido):
        Profesor._secuencia += 1
        self.__id = Profesor._secuencia
        self.nombre = nombre
        self.apellido = apellido

    @property
    def id(self):
        return self.__id

    def mostrar(self):
        print("Profesor:")
        print(f"ID: {self.id} - Nombre: {self.nombre} -  Apellido: {self.apellido}\n")

class Alumno:
    _secuencia = 0

    def __init__(self, nombre, apellido):
        Alumno._secuencia += 1
        self.__id = Alumno._secuencia
        self.nombre = nombre
        self.apellido = apellido
        self.notas = []  # Agregación: Alumno contiene registros de notas

    @property
    def id(self):
        return self.__id

    def agregar_notas(self, notas):
        self.notas.append(notas)

    def mostrar(self):
        print("Alumno:")
        print(f"ID: {self.id} - Nombre: {self.nombre} - Apellido: {self.apellido}\n")
        #print("REGISTRO DE NOTAS")
        for notas in self.notas:
            notas.mostrar()

class Semestre:
    _secuencia = 0

    def __init__(self, descripcion, seccion, paralelo, fecha_inicio, fecha_fin):
        Semestre._secuencia += 1
        self.__id = Semestre._secuencia
        self.descripcion = descripcion
        self.paralelo = paralelo
        self.seccion = seccion
        self.fechaInicio = fecha_inicio
        self.fechaFin = fecha_fin

    @property
    def id(self):
        return self.__id

    def mostrar(self):
        print("Nivel:")
        print(f"ID: {self.id} - Descripción: {self.descripcion} - Sección: {self.seccion} - Paralelo: {self.paralelo} - Fecha de Inicio: {self.fechaInicio.strftime('%Y-%m-%d')} - Fecha de Fin: {self.fechaFin.strftime('%Y-%m-%d')}\n")

class Carrera:
    _secuencia = 0

    def __init__(self, nombre):
        Carrera._secuencia += 1
        self.__id = Carrera._secuencia
        self.nombre = nombre

    @property
    def id(self):
        return self.__id

    def mostrar(self):
        print("Carrera:")
        print(f"ID: {self.id} - Nombre: {self.nombre}\n")

class Facultad:
    _secuencia = 0

    def __init__(self, nombre):
        Facultad._secuencia += 1
        self.__id = Facultad._secuencia
        self.nombre = nombre
        self.carreras = []  

    def agregar_carrera(self, nombre_carrera):
        carrera = Carrera(nombre_carrera) #Composicion 
        self.carreras.append(carrera)

    @property
    def id(self):
        return self.__id

    def mostrar(self):
        print("Facultad")
        print(f"ID: {self.id} - Nombre: {self.nombre}\n")
      
        for carrera in self.carreras:
            carrera.mostrar()

class Notas:
    _secuencia = 0

    def __init__(self, facultad, carrera, asignatura, profesor, alumno, semestre, nota1, nota2, examen1, parcial1, nota3, nota4, examen2, parcial2, nota_final, estado):
        Notas._secuencia += 1
        self.__id = Notas._secuencia
        self.facultad = facultad
        self.carrera = carrera
        self.asignatura = asignatura
        self.profesor = profesor
        self.alumno = alumno
        self.semestre = semestre 
        self.nota1 = nota1
        self.nota2 = nota2
        self.examen1 = examen1
        self.parcial1 = parcial1
        self.nota3 = nota3
        self.nota4 = nota4
        self.examen2 = examen2
        self.parcial2 = parcial2
        self.nota_final = nota_final
        self.estado = estado

    @property
    def id(self):
        if self.__id == 0:
            return -1
        else:
            return self.__id 

    def mostrar(self):
        print("REGISTRO DE NOTAS")
        print(f"ID: {self.id}")
        print(f"Facultad: {self.facultad.nombre}")
        print(f"Carrera: {self.carrera.nombre}")
        print(f"Semestre: {self.semestre.descripcion}")
        print(f"Inicio: {self.semestre.fechaInicio.strftime('%Y-%m-%d')} Fin: {self.semestre.fechaFin.strftime('%Y-%m-%d')}")
        print(f"Sección: {self.semestre.seccion}")
        print(f"Paralelo: {self.semestre.paralelo}")
        print(f"Asignatura: {self.asignatura.nombre}")
        print(f"Profesor: {self.profesor.nombre} {self.profesor.apellido}\n")

        print("Calificaciones:")
        print(f"Alumno: {self.alumno.nombre} {self.alumno.apellido}")
        print(f"N1: {self.nota1}")
        print(f"N2: {self.nota2}")
        print(f"Examen 1: {self.examen1}")
        print(f"Parcial 1: {self.parcial1}")
        print(f"N3: {self.nota3}")
        print(f"N4: {self.nota4}")
        print(f"Examen 2: {self.examen2}")
        print(f"Parcial 2: {self.parcial2}")
        print(f"Nota Final: {self.nota_final}")
        print(f"Estado: {'Aprobado' if self.estado else 'Reprobado'}\n") 

facultad = Facultad("Facultad de Ciencias e Ingeniería")
facultad.agregar_carrera("Software") #Composicion entre Facultad y Carreras
asignatura = Asignatura("Algoritmos y Lógica de Programación")
profesor = Profesor("Daniel", "Vera")
alumno = Alumno("Ruben", "Guiterrez")
fecha_inicio = date(2023, 8, 24)
fecha_fin = date(2023, 12, 20)
semestre = Semestre("Primer Semestre 2023", "Nocturno", "C1", fecha_inicio, fecha_fin)
nota1 = Notas(facultad, facultad.carreras[0], asignatura, profesor, alumno, semestre, 13.75, 14.0, 7.0, 34.75, 11.25, 14.0, 10.0, 35.25, 70.0, True) #Agregacion de entidades a Notas
alumno.agregar_notas(nota1)

nota1.mostrar() #Mostrar el registro de notas

#facultad.mostrar()
#asignatura.mostrar()
#semestre.mostrar()
#profesor.mostrar()
#alumno.mostrar()





