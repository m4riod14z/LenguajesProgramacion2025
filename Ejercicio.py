# Aproximacion de el numero de euler
from math import factorial
from functools import reduce
n = int(input("Ingrese la cantidad de terminos que desea: "))

nums = list(range(0, n+1))

def fun_map(n):
    return 1 / factorial(n)

def fun_redux(a,b):
    return a+b

aprox = reduce(fun_redux, list(map(fun_map, nums)))
print(f"Aproximacion de e: {aprox} ")