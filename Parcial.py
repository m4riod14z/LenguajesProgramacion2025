from functools import reduce

# Leer datos
def loadData(filePath):
    with open(filePath, mode="r", encoding="utf-8") as file:
        header = file.readline().strip().split(",")
        for line in file:
            values = line.strip().split(",")
            record = dict(zip(header, values))
            yield record


dataStream = loadData("personajes.csv")

personajes = []
try:
    for personaje in range(10):
        personajes.append(next(dataStream))
except StopIteration:
    print("\nDiccionario de personajes:")

print(personajes)

# Filtrar personajes con nivel > 10
print("\nPersonajes con nivel mayor a 10:")
listaPersonajes = list(filter(lambda x: int(x["nivel"])>10, personajes))
print(listaPersonajes)

# Lista totalPower
print("\nLista con totalPower:")
totalPower = list(map(lambda x: dict(x, totalPower=int(x["ataque"]) + int(x["defensa"])), listaPersonajes))
print(totalPower)

# Poder total
def comparar_poder_total(x, y):
    totalPower_x = int(x["ataque"])+int(x["defensa"])
    totalPower_y = int(y["ataque"])+int(y["defensa"])
    
    if totalPower_x > totalPower_y:
        return x
    else:
        return y


print("\nPersonaje con mayor poder total:")
personajePowerful = reduce(comparar_poder_total, totalPower)
print(personajePowerful)