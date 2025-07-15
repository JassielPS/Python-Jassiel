# Ejemplo 1: Retorno simple
def cuadrado(x):
    return x ** 2

print("Cuadrado de 5:", cuadrado(5))

# Ejemplo 2: Retorno múltiple
def operaciones(a, b):
    return a + b, a - b, a * b

suma, resta, multiplicacion = operaciones(10, 5)
print(f"Suma: {suma}, Resta: {resta}, Multiplicación: {multiplicacion}")

# Ejemplo 3: Retorno condicional
def es_mayor_edad(edad):
    return True if edad >= 18 else False

print("¿Mayor de edad?", es_mayor_edad(20))
