# Ejemplo 1: Variable global
contador = 0

def incrementar():
    global contador
    contador += 1

incrementar()
print("Contador:", contador)

# Ejemplo 2: Variable local
def funcion_local():
    variable_local = "Hola"
    print(variable_local)

funcion_local()

# Ejemplo 3: No se puede acceder a local desde fuera
# print(variable_local)  # Error...XD
