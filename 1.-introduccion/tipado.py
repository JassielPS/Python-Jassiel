# Ejemplo 1: Tipado dinámico
variable = 10
variable = "ahora string"
print(variable)

# Ejemplo 2: Type hints
def suma(a: int, b: int) -> int:
    return a + b

# Ejemplo 3: Comprobación
if type(variable) == str:
    print("Es string...XD")
