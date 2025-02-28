# Lazy Evaluation / Generadores
# Procesamiento de flujos de datos (Streams)
import random
def lazyRandomGenerator():
    while True:
        # La instruccion Yield devuelve el valor (es un return) pero espera el "next"
        # del consumidor
        yield random.randint(1, 1000)

generadorAleatorios = lazyRandomGenerator()
# print(next(generadorAleatorios))
# print(next(generadorAleatorios))
# print(next(generadorAleatorios))

for _ in range(100):
    # Cuando se invoca el next del generador, el generador devuelve un valor
    # y espera el siguiente next con Yield
    print(next(generadorAleatorios))