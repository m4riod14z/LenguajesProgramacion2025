# Aproximacion de el numero de euler
from math import factorial
from functools import reduce
n = int(input("Ingrese la cantidad de terminos que desea: "))

nums = list(range(0, n+1))
x = int(input("Ingrese el valor de X que desea: "))

def fun_map(n):
    return (x**n) / factorial(n)

def fun_redux(a,b):
    return a+b

aprox = reduce(fun_redux, list(map(fun_map, nums)))
print(f"Aproximacion de e^{x}: {aprox}")