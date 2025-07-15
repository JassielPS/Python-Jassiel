# Ejemplo 1: Múltiples asignaciones
x, y, z = 1, 2, 3
print(x + y + z)

# Ejemplo 2: Intercambio de valores
a, b = 10, 20
a, b = b, a
print(f"a={a}, b={b}")

# Ejemplo 3: Múltiples returns
def coordenadas():
    return 10, 20, 30
x, y, z = coordenadas()
print(z)
