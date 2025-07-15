# Ejemplo 1: Función simple
def saludar():
    print("Hola mundo...XD")

saludar()

# Ejemplo 2: Función con parámetros
def sumar(a, b):
    return a + b

print("Suma:", sumar(5, 3))

# Ejemplo 3: Función con valor por defecto
def saludar_persona(nombre="Jassiel"):
    print(f"¡Hola, {nombre}!")

saludar_persona()
saludar_persona("Ana")
