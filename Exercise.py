# Generador "perezoso" de multiplos de m
# Genera uno a la vez: Yield lo retorna y espera a que le pidan el siguiente

def multN(m):
    num = 0
    while True:
        if num % m == 0:
            # El productor entrega un dato y espera a que le pidan mas (perezoso)
            yield num
        num = num+1

generadorMultiplos = multN(7)
# El consumidor tambien es "perezoso", pide un dato a la vez

# print(next(generadorMultiplos))
# print(next(generadorMultiplos))
# print(next(generadorMultiplos))

# Al usar un generador en un ciclo, se debe usar un try except:
try:
    for _ in range(100):
        print(next(generadorMultiplos))
except StopIteration:
    print("Se ha producido un error consumiendo datos del generador")