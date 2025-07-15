# Ejemplo 1: Atributos y métodos
class Cafe:
    # Atributo de clase
    tipo = "Bebida"

    # Método de instancia
    def __init__(self, nombre):
        self.nombre = nombre

    def describir(self):
        print(f"Café {self.nombre}...XD")

# Ejemplo 2: Uso
mi_cafe = Cafe("Latte")
mi_cafe.describir()

# Ejemplo 3: Acceso a atributo de clase
print("Tipo:", Cafe.tipo)
