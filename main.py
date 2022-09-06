from helpers import Helper
from modulos.funciones_matematicas import *
from paquete1.funciones_cadena import contar_letras
from paquete1.funciones_numericas import *
from POO.Persona import *
from POO.Curso import *
from POO.Cuenta import *
from POO.Herencia import *
from POO.HerenciaMultiple import *
from POO.Polimorfismo import *
from POO.RelacionesClases import *
import os

#Repite el listado
helper = Helper()
lista = ["1) Hola Mundo","2) Variables","3) Conversiones","4) Numeros y Operaciones","5) Concatenación","6) Cadenas","7) Tuplas","8) Listas","9) Diccionarios","10) Lectura de Datos","11) Estructura Condicional","12) Funciones","13) Operadores Lógicos","14) Operadores Ternarios ","15) Funcion Range","16) Bucle For","17) If con Tuplas y Listas","18) Factorial de un número","19) Bucle While","20) Sentencia Break, Continue y Pass","21) Generadores","22) Generadores 2","23) Excepciones","24) Sentencia Raise","25) Módulos","26) Paquetes","27) Poo","28) Curso y __str__","29) Método Accesores","30) Herencia, sobreescritura de Métodos y Principio de Sustitución","31) Herencia Multiple","32) Polimorfismo","33) Relaciones entre Clases","34) Salir"]
opcion=""

#EJERCICIOS PYTHON
while opcion != "34":
  os.system("cls")
  opcion = helper.menu(lista,"*"*20+" EJERCICIOS PYTHON "+"*"*20)

  #EJERCICIOS
  if opcion == "1":
    print("Hola Mundo")
    input("Presione una tecla para continuar...")

  elif opcion == "2":
    nombre = "UskoKruM2010"
    print(nombre)
    edad = 25
    print(edad)
    edad = True
    print(edad)
    sueldo = 205.10
    print(sueldo)
    input("Presione una tecla para continuar...")

  elif opcion == "3":
    numero1 = "35"
    numero2 = "18"
    print(numero1 + numero2)
    num1 = int(numero1)
    num2 = int(numero2)
    print(num1 + num2)
    sueldo = 1200.43
    sueldoEntero = int(sueldo)
    print(sueldoEntero)
    valor = "4500.89"
    valorDecimal = float(valor)
    print(valorDecimal * 3 )
    edad = 100
    print(len(str(edad)))
    input("Presione una tecla para continuar...")

  elif opcion == "4":
    entero = 23
    decimal = 31.78
    entero = 12 + 5j
    # booleano = True
    '''
    print(entero) 
    print(decimal)
    print(complejo)
    print(booleano)
    '''
    num1 = 20
    num2 = 4
    print("Suma:", (num1 + num2))
    print("Resta:", (num1 - num2))
    print("Multiplicación:", (num1 * num2))
    print("División:", (num1 / num2))
    print("División Exacta:", (num1 // num2))
    print("Potencia:", (num1 ** num2))
    input("Presione una tecla para continuar...")

  elif opcion == "5":
    texto1 = "Hola"
    texto2 = "Mundo"
    textoFinal = texto1 + " " + texto2
    print(textoFinal)
    print("El saludo es: %s %s" % (texto1, texto2))
    saludoFinal = "Saludo: {0} {1}".format(texto1,texto2)
    print(saludoFinal)
    saludoFinal2 = "Saludo: {y} {x}".format(x=texto2, y=texto1)
    print(saludoFinal2)
    input("Presione una tecla para continuar...")

  elif opcion == "6":
    texto = "bienveNIdos al canal de uskokrum2010"
    print(texto)
    print(texto.lower())
    print(texto.upper())
    print(texto.title())  # Convierte una cadena a un formato de título.
    print(texto.find("al"))  # Posición donde encuentra la cadena o porción.
    print(texto.count("e"))  # Cantidad de ocurrencias de una letra o porción.
    textoFinal = texto.replace("e", "3")
    print(textoFinal)
    valor = texto.isnumeric()  # Arroja true o false dependiendo si es un número.
    print(valor)
    cadenaSeparada = texto.split(" ")
    print(cadenaSeparada)
    input("Presione una tecla para continuar...")

  elif opcion == "7":
    """
    Tupla: Es una estructura de datos propia de Python que permite almacenar distintos
    valores, son inmutables: no cambian una vez inicializadas.
    """
    tupla = (1, 2, 3)
    print(tupla)
    tupla2 = (7, "Oscar", True, 450.1, 16 + 7j, 15, "Felicidad", False)
    print(tupla2)
    tupla3 = (9, 3, (4, 5, 6))
    print(tupla3)
    print(tupla2[1])
    # tupla2[1] = "UskoKruM"
    print(tupla2[-1])  # Acceder al último elemento.
    print(tupla2[0:4])
    print(tupla2[-2])
    a, b, c = tupla
    print(a)
    print(b)
    print(c)
    tuplaFinal = tupla + tupla3
    print(tuplaFinal)
    print(tuplaFinal.count(21))
    print(tuplaFinal.index(3))
    input("Presione una tecla para continuar...")

  elif opcion == "8":
    # Listas: Son estructuras de datos que nos permiten almacenar distintos valores
    # (equivalentes a los arrays en otros lenguajes de programación)
    # Son estructuras dinámicas, pueden MUTAR.
    lista1 = ["Oscar", 25, 98.3, True, "Flavio", 56.3]
    print(lista1)
    print(lista1[:])
    print(lista1[2])
    print(lista1[-1])
    print(lista1[0:3])
    print(lista1[:2])
    print(lista1[3:])
    lista1.append("UskoKruM2010")
    print(lista1)
    lista1.insert(4, "Perú")
    print(lista1)
    lista1.extend(["Alejandro", 110, False])
    print(lista1)
    print(lista1.index("Flavio"))
    lista1.remove(56.3)
    print(lista1)
    lista1.pop()
    print(lista1)
    lista2 = ["Chiclayo", "Irma"]
    lista3 = lista1 + lista2
    print(lista3)
    print(lista2 * 4)
    print("UskoKruM2010" in lista1)
    input("Presione una tecla para continuar...")

  elif opcion == "9":
    # Diccionarios: Son estructuras de datos que nos permiten almacenar distintos
    # valores.
    # Es que los datos se almacenan asociados a una clave única, tenemos una relación
    # clave:valor
    # Los elementos almacenados están en desorden, el orden es indiferente a la forma
    # de almacenamiento.
    miDiccionario = {"España": "Madrid", "Perú": "Lima", "Alemania": "Berlín"}
    print(miDiccionario["Perú"])
    print(miDiccionario)
    miDiccionario["Venezuela"] = "Caracas"
    print(miDiccionario)
    miDiccionario["España"] = "Barcelona"
    print(miDiccionario)
    del miDiccionario["España"]
    print(miDiccionario)
    dic2 = {"García": "Oscar", 25: True, "Sueldo": 150.80}
    print(dic2[25])
    llaves = ("España", "Francia", "Inglaterra")
    dicPaises = {llaves[0]: "Madrid", llaves[1]: "París", llaves[2]: "Londres"}
    print(dicPaises)
    datosPersonales = {"Ape": "García", "Anios": {1: 2010, 2: 2011, 3: 2012, 4: 2013, 5: 2014}}
    print(datosPersonales)
    print(datosPersonales["Anios"])
    print(datosPersonales.get('Apel', "Oscar"))
    print(datosPersonales.keys())
    valores = tuple(datosPersonales.values())
    print(valores)
    input("Presione una tecla para continuar...")

  elif opcion == "10":
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))
    sueldo = float(input("Ingrese su sueldo: "))
    print("Hola, " + nombre)
    edadFutura = edad + 20
    print("Tu edad es:", edad)
    print("Tu edad (dentro de 20 años) será:", edadFutura)
    print("Tu sueldo es:", sueldo)
    input("Presione una tecla para continuar...")

  elif opcion == "11":
    edad = int(input("Ingrese su edad: "))
    if edad > 18:
      print("Eres mayor de edad.")
    elif edad == 18:
      print("Tienes 18 años!")
    else:
      print("No eres mayor de edad.")
    input("Presione una tecla para continuar...")

  elif opcion == "12":
    # Función: Es un conjunto de instrucciones que realizan un proceso.
    # Su principal ventaja es que nos ayudan a evitar código repetido.
    def saludar():
      print("García")
      print("Oscar")
      print("UskoKruM2010")
      return "Hola"
    print(saludar())
    def evaluarSueldoMinimo(sueldo):
      if sueldo >= 850:
        print("Cumples con el sueldo")
      else:
        print("Ganas menos que el sueldo mínimo")
    evaluarSueldoMinimo(100)
    input("Presione una tecla para continuar...")

  elif opcion == "13":
    # AND: Equivalente a "Y si además..."
    # OR: "O sino..."
    # not -> negación
    distancia = 400
    numeroHermanos = 3
    salarioPadres = 3000
    tieneBeneficio = False
    if (distancia > 1000 and numeroHermanos > 2) or salarioPadres < 2000:
      tieneBeneficio = True
    print(not tieneBeneficio)
    if (5 > 3) or (8 < 6):
      print("Verdad")
    else:
      print("Es mentira...")
    input("Presione una tecla para continuar...")

  elif opcion == "14":
    """
    String sexo;
    sexo = (10 > 20) ? "Masculino" : "Femenino";
    """
    sexos = ("Hombre", "Mujer")
    posicion = True
    sexo = sexos[posicion]  # Mujer
    print(sexo)
    sexo = sexos[not posicion]  # Hombre
    print(sexo)
    input("Presione una tecla para continuar...")

  elif opcion == "15":
    # range(): Crea una lista inmutable de números enteros en sucesión aritmética.
    numeros = range(5)  # [0, 1, 2, 3, 4]
    print(numeros[1])
    numeros1 = range(4, 10)  # [4, 5, 6, 7, 8, 9]
    print(numeros1[5])
    numeros2 = range(10, 100, 8)
    print(numeros2[9])  # [10, 18, 26, 34, 42, 50, 58, 66, 74, 82, 90, 98]
    input("Presione una tecla para continuar...")

  elif opcion == "16":
    # Bucles: Son estructuras de control de flujo que repiten 1 o varias líneas de código.
    """
    for num in range(0, 20, 2):
        print("Valor actual: {0}".format(num))
    """
    for i in range(1, 13):
      print("{0} x {1} es: {2}".format(i, i, (i * i)))
    for nom in ["Karen", "Oscar", "Héctor", "Leonardo"]:
      print("Cantidad de letras de {0} es: {1}".format(nom, len(nom)))
    input("Presione una tecla para continuar...")

  elif opcion == "17":
    print("-- Cursos --")
    print("Matematica - Biologia - Lenguaje - Ciencias")
    curso = input("Ingrese el curso deseado: ")
    if curso in ("Matematica", "Biologia", "Lenguaje", "Ciencias"):
      print("Curso {0} seleccionado.".format(curso))
    else:
      print("No existe ese curso...")
    input("Presione una tecla para continuar...")

  elif opcion == "18":
    # Factorial: Es el producto de todos los números positivos enteros comprendidos entre 1 y un número.

    # Factorial de 5: 1 * 2 * 3 * 4 * 5 = 120
    # Factorial de 4: 1 * 2 * 3 * 4 = 24

    numero = int(input("Ingrese un número: "))

    factorial = 1
    for n in range(1, (numero + 1)):
      factorial = factorial * n

    print("El factorial de {0} es: {1}".format(numero, factorial))

    input("Presione una tecla para continuar...")

  elif opcion == "19":
    # While: Estructura repetitiva que nos permite realizar múltiples iteraciones
    # basándonos en el resultado de una expresión lógica que puede
    # tener como resultado un valor True o False.

    """
    indice = 1

    while indice < 10:
        print("Valor actual: {0}".format(indice))
        indice = indice + 1

    print("Hemos terminado el bucle while.")
    # Continua el programa.
    """

    inicio = 2

    while inicio <= 100:
      print("Número par: {0}".format(inicio))
      inicio += 2

    print("Hemos terminado el bucle while.")
    input("Presione una tecla para continuar...")

  elif opcion == "20":
    # Break: Permite salir de un bucle cuando se cumple una condición.

    """
    for numero in range(1, 6):
        if numero == 3:
            break  # Descanso o interrupción en este punto.
        print("El número es: {0}".format(numero))

    print("Bucle terminado.")
    """

    # Continue: Omite una parte del bucle cuando se cumple una condición y
    # continúa con el resto.

    """
    for numero in range(1, 6):
        if numero == 3:
            continue  # Continúa con el resto del bucle.
        print("El número es: {0}".format(numero))

    print("Bucle terminado.")
    """

    # Pass: Permite continuar con una sentencia o función que ya no tiene
    # o aún no tiene un bloque de código útil.

    for numero in range(1, 6):
      if numero <= 3:
        # Aquí no pasa nada y el bucle sigue trabajando.
        pass
      else:
        print("El siguiente valor es mayor a 3:")
      print("El número es: {0}".format(numero))

    print("Bucle terminado.")


    def funcionSinImplementar():
      pass
    input("Presione una tecla para continuar...")

  elif opcion == "21":
    # Generadores: Permiten extraer valores de una función y almacenarlo
    # (de uno en uno) en objetos iterables (que se pueden recorrer),
    # sin la necesidad de almacenar TODOS A LA VEZ en la memoria RAM.

    """
    def generaMultiplos7(limite):
        numero = 1
        listaNumeros = []

        while numero <= limite:
            listaNumeros.append(numero * 7)
            numero = numero + 1
        return listaNumeros  # Retorna toda la lista creada.

    print(generaMultiplos7(10))
    """


    def generadorMultiplos7(limite):
      numero = 1

      while numero <= limite:
        yield numero * 7  # Ceder. La instrucción "yield" genera un objeto iterable.
        numero = numero + 1


    obtieneMultiplos7 = generadorMultiplos7(10)

    """
    # print(obtieneMultiplos7)
    for n in obtieneMultiplos7:
        print(n)
    """

    # next(): Retorna el siguiente elemento de un objeto iterable:

    print(next(obtieneMultiplos7))
    print("Acá hay 300 líneas de código...")
    print(next(obtieneMultiplos7))
    print("Acá hay 1000 líneas de código...")
    print(next(obtieneMultiplos7))

    # Son más eficiente que las funciones tradicionales.
    # Muy útiles con listas de valores infinitos.
    # Entre llamada y llamada, el objeto iterable entra en un estado de pausa (suspensión).
    input("Presione una tecla para continuar...")

  elif opcion == "22":
    # Cuando indicamos un * adelante del parámetros de una función,
    # estamos indicado que se va a recibir un número indeterminado
    # de parámetros. Además, esos parámetros se recibirán en forma de tupla.

    """
    def devuelveLenguajes(*lenguajes):
        for leng in lenguajes:
            yield leng
    """


    def devuelveLenguajes(*lenguajes):
      for leng in lenguajes:
        yield from leng


    lenguajesObtenidos = devuelveLenguajes("Python", "Java", "PHP", "Ruby", "JavaScript")

    print(next(lenguajesObtenidos))
    print(next(lenguajesObtenidos))
    input("Presione una tecla para continuar...")

  elif opcion == "23":
    # Excepción: Error en tiempo de ejecución (durante la ejecución de un programa).

    numero1 = 20
    numero2 = 2

    # print("La división de {0} entre {1} es: {2}".format(numero1, numero2, (numero1 / numero2)))

    try:
      resultado = numero1 / numero2
    # except:
    except ZeroDivisionError:
      print("No se puede dividir entre 0...")
    finally:
      print("Yo siempre aparezco.")

    print("Aquí termina mi programa.")

    input("Presione una tecla para continuar...")

  elif opcion == "24":
    # Raise: Sirve para lanzar (de forma intencional) excepciones en Python.

    def evaluarNota(nota):
      if nota < 0:
        raise ValueError("Valor incorrecto...")
        # raise ZeroDivisionError("Este mensaje es personalizado.")
      elif nota >= 16:
        print("Excelente")
      elif nota >= 11:
        print("Aprobado")
      else:
        print("Desaprobado")


    evaluarNota(-7)

    print("Este es el fin de mi programa.")
    input("Presione una tecla para continuar...")

  elif opcion == "25":
    print(sumar(5, 6))
    print(multiplicar(5, 6))
    input("Presione una tecla para continuar...")

  elif opcion == "26":
    print(multiplicar(5, 6))
    print(contar_letras("UskoKruM2010"))
    input("Presione una tecla para continuar...")

  elif opcion == "27":
    persona1 = Persona()
    persona1.apellidos = "García Fuentes"
    print(persona1.apellidos)
    persona1.despertar()
    print(persona1.despierta)

    persona2 = Persona()
    persona2.apellidos = "Paz Torres"
    print(persona2.apellidos)
    # persona2.despertar()
    print(persona2.despierta)
    input("Presione una tecla para continuar...")

  elif opcion == "28":
    curso1 = Curso("Matemática", 5, "Ingeniería Civil")
    print(curso1)
    curso1.mostrarDatos()
    input("Presione una tecla para continuar...")

  elif opcion == "29":
    cuenta1 = Cuenta("Oscar García", 15000, "Soles")
    print(cuenta1.get_Saldo())
    print(cuenta1.get_Moneda())
    cuenta1.set_Moneda("Dólares")
    print(cuenta1.get_Moneda())
    input("Presione una tecla para continuar...")

  elif opcion == "30":
    estu1 = Estudiante("Torres", "López", "Juan", "Ingeniería Civil")
    print(estu1.mostrarNombreCompleto())
    input("Presione una tecla para continuar...")

  elif opcion == "31":
    cX1 = ClaseX(15, 21)
    input("Presione una tecla para continuar...")

  elif opcion == "32":
    doc1 = Trabajador()
    describirPersona(doc1)
    input("Presione una tecla para continuar...")

  elif opcion == "33":
    pais1 = Pais("Perú", "Martín Vizcarra")
    print(pais1)

    ciudad1 = Ciudad("Chiclayo", 150000, pais1)
    print(ciudad1)

    urba1 = Urbanizacion("María de los Angeles", ciudad1)
    print(urba1)
    input("Presione una tecla para continuar...")
  elif opcion == "34":
    print("Ejercicios Terminados")
    input("Presione una tecla para FINALIZAR...")