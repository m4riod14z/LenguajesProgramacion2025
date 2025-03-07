# 1. Leer datos CSV
# 2. Crear dataset (lista de diccionarios)
# 3. Entregar un registro a la vez (yield, evaluación perezosa)
# 4. Ir filtrando (filter) / post-procesando (map) datos recibidos

from functools import reduce

# Lector de datos de un csv que funciona como un generador para un evaluador perezoso:
def loadData(filePath):
    with open(filePath, mode="r", encoding="utf-8") as file:
        header = file.readline().strip().split(",") # Leer encabezado como las claves del diccionario
        for line in file:
            values = line.strip().split(",")
            record = dict(zip(header, values)) # Dict: Crea un diccionario vacío, Zip: Recibe una lista de llaves y otra de valores y los une como una tupla
            yield record

def USD_to_COP(salario):
    salario["Salario"] = int(salario["Salario"])*4100
    return salario

dataStream = loadData("dataset.csv")

# Consumir registros
dataLocal = []
try:
    for __ in range(1000):
        dataLocal.append(next(dataStream))
except StopIteration:
    print("Error")

print(dataLocal)

# Convertir campo "Salario" de USD a COP mapeando una funcion de conversion de divisas:
# 1 USD = 4105 COP
listaSalarioPesos = list(map(USD_to_COP, dataLocal))
print("\nEmpleados con salarios en COP:")
print(listaSalarioPesos)

# Filtrar aquellos que tengan un salario mayor a $COP 7'000.000:
listaMayores = list(filter(lambda x: int(x["Salario"])>7000000, listaSalarioPesos))
print("\nEmpleados con salarios mayores a 7'000.000:")
print(dataLocal)

# Sumar el total de salario de esas personas con Reduce:
sumaTotal = reduce(lambda a,b: a+int(b["Salario"]), listaMayores, 0)
print(f"El total de todos los salarios es: {sumaTotal}")