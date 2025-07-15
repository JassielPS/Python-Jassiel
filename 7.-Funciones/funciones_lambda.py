# Ejemplo 1: Lambda básica
cuadrado = lambda x: x ** 2
print("Cuadrado de 4:", cuadrado(4))

# Ejemplo 2: Lambda con múltiples parámetros
suma = lambda a, b: a + b
print("Suma:", suma(5, 3))

# Ejemplo 3: Uso con map()
numeros = [1, 2, 3]
dobles = list(map(lambda x: x * 2, numeros))
print("Dobles:", dobles)
