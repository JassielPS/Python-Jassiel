# Ejemplo 1: Constructor
class Cafe:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def describir(self):
        print(f"{self.nombre} - ${self.precio}")

# Ejemplo 2: Instancia con parámetros
cafe1 = Cafe("Capuchino", 50)
cafe1.describir()

# Ejemplo 3: Acceso a atributos
print(f"Precio: {cafe1.precio}")
