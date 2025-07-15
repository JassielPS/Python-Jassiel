# Ejemplo 1: Velocidad
import timeit
print("Tupla:", timeit.timeit('(1,2,3)'))
print("Lista:", timeit.timeit('[1,2,3]'))

# Ejemplo 2: Uso como clave
clave = (1, "a")
diccionario = {clave: "valor"}
print(diccionario[(1, "a")])

# Ejemplo 3: Mutabilidad
lista = [1, 2, 3]
tupla = tuple(lista)
lista[0] = 99
print("Lista modificada:", lista)
print("Tupla inmutable:", tupla)
