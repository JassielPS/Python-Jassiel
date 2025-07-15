# Ejemplo 1: Argumentos posicionales
def resta(a, b):
    return a - b

print("Resta:", resta(10, 5))

# Ejemplo 2: Argumentos nombrados
print("Resta:", resta(b=5, a=10))

# Ejemplo 3: Parámetros arbitrarios (*args)
def sumar_todo(*args):
    return sum(args)

print("Suma total:", sumar_todo(1, 2, 3))
