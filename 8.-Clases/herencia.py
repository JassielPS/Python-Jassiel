# Ejemplo 1: Herencia
class Bebida:
    def __init__(self, nombre):
        self.nombre = nombre

    def servir(self):
        print("Sirviendo bebida...")

class Cafe(Bebida):
    def __init__(self, nombre, tipo):
        super().__init__(nombre)
        self.tipo = tipo

    def describir(self):
        print(f"Café {self.nombre} ({self.tipo})")

# Ejemplo 2: Uso
mi_cafe = Cafe("Latte", "Caliente")
mi_cafe.servir()
mi_cafe.describir()

# Ejemplo 3: Sobrescritura de método
class Te(Bebida):
    def servir(self):
        print("Sirviendo té con estilo...XD")

mi_te = Te("Verde")
mi_te.servir()
