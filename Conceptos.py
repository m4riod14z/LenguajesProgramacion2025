#Conceptos de programacion funcional

#1. Funciones son ciudadanos de primer orden: Parametros. retornos, asignar variables

def suma(a, b):
    return a+b

def resta(a, b):
    return a-b

def multiplicacion(a, b):
    return a*b

def division(a, b):
    if b != 0:
        return a/b

val1 = int(input("Ingrese el primer valor: "))
val2 = int(input("Ingrese el segundo valor: "))
opt = int(input("Ingrese la operacion: 1. Suma 2. Resta 3. Multiplicacion 4. Division"))

if opt == 1:
    operacion = suma
elif opt == 2:
    operacion = resta
elif opt == 3:
    operacion = multiplicacion
elif opt == 4:
    operacion = division
else:
    print("Operacion no valida")

print(f"El resultado es: {operacion(val1, val2)}")

#2. Funciones puras: Solo usan parametros para recibir valores, no tocan variables globales
# con las mismas entradas, producen mismos resultados (como ejemplo las operaciones de arriba)
# Si toca variables globales o modifica los valores de entrada (generar nuevos datos), la funcion no es pura

#3. Funciones anonimas (lambda): Una funcion en terminos genericos
# lambda x: x % 2 == 0, recibe un parametro y retorna la evaluacion, tiene las mismas caracteristicas
# de una funcion

num = int(input("Ingrese un numero cualquiera: "))
es_par = lambda x: x % 2 == 0
print(f" {num} es par?: {es_par(num)}")

#4. Funciones de orden superior:
# Son funciones que reciben como parametros otras funciones o devolverlas
# a. Funcion MAP: Genera una nueva lista aplicando una funcion definida sobre otra

# b. Funcion FILTER: Genera una nueva lista, aplicando una funcion de filtro booleano (True or False)
#                     a cada uno de los elementos de la lista original

# c. Funcion REDUCE: Aplica una funcion a cada uno de los elementos de una
#                     lista, devolviendo un solo valor

#Forma larga:
#Es una funcion pura?
# Si es pura porque no toca variables, globales y los datos de entrada no son modificados para nada
# Solo se crea una copia

ciudades = ["Cali", "medellin", "BOGOTA", "bArrAnQuillA"]

def normalizar_datos(lista_nombres):
    datos_norm = []
    for nombre in lista_nombres:
        datos_norm.append(nombre.capitalize())
    return datos_norm

ciudades_norm = normalizar_datos(ciudades)
print(f"Ciudades sin normalizar: {ciudades}")
print(f"Ciudades normalizadas: {ciudades_norm}")

# Ejemplo con la funcion map, sin funcion lambda
def capitalizar(palabra):
    return palabra.capitalize() #capitalize es para retornar la palabra con la inicial en mayuscula

ciudades_norm2 = list(map(capitalizar, ciudades))
print(f"Datos normalizados: {ciudades_norm2}")

#Ejemplo con la funcion map, usando lambda
ciudades_norm3 = list(map(lambda n: n.capitalize(), ciudades))
print(f"Datos normalizados: {ciudades_norm3}")

# Funcion de orden superior definida por el usuario:
def aplicar_operacion(operacion, operando1, operando2):
    return aplicar_operacion(operando1, operando2)

print(f"El resultado es: {operacion(val1, val2)}")
print(f"El resultado es: {aplicar_operacion(operacion, val1, val2)}")

# Uso de la funcion FILTER:
# Filter aplica una funcion booleana sobre una lista de objetos y devuelve una lista más pequeña
# que contiene solo los objetos para los cuales la funcion booleana devuelve True.

# edades = [12, 14, 18, 19, 24, 25, 28]
personas = [{"nombre": "Mario", "edad": "17"},
            {"nombre": "Maria", "edad": "21"},
            {"nombre": "Catalina", "edad": "16"},
            {"nombre": "Manuel", "edad": "34"},]


# def filtrar_mayores_edad(edad):
    # return edad >= 18

def filtrar_personas_mayores(persona):
    return int(persona["edad"]) >= 18


# mayores_edad = list(filter(filtrar_mayores_edad, edades))
# print(f"Edades mayores a 18: {mayores_edad}")

personas_mayores = list(filter(filtrar_personas_mayores, personas))
print(f"Personas mayores: {personas_mayores}")

# Funcion REDUCE:
# Consolida los elementos de una lista usando una funcion que se aplica por cada par de elementos:
from functools import reduce
numeros = list(range(1, 101)) #Generar una lista de numeros de 1 a 100

# Sumarlos con un iterador:
sum = 0
for i in numeros:
    sum = sum + i

print(sum)

# Sumar con REDUCE:
suma = reduce(lambda x,y: x+y, numeros)
print(suma)

palabras = ["en", "un", "lugar"]
texto = reduce(lambda a,b: a+" "+b, palabras)
print(texto)