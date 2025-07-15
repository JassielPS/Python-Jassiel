# Ejemplo 1: Crear objetos
class Cliente:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"Cliente: {self.nombre}, Edad: {self.edad}"

# Ejemplo 2: Lista de objetos
clientes = [
    Cliente("Jassiel", 25),
    Cliente("Ana", 30)
]

# Ejemplo 3: Recorrer y usar
for cliente in clientes:
    print(cliente)
