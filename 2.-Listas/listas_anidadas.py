# Ejemplo 1: Matriz
matriz = [[1, 2], [3, 4]]
print(matriz[0][1])  # 2

# Ejemplo 2: Lista de diccionarios
menu = [{"nombre": "Espresso", "precio": 45}, {"nombre": "Latte", "precio": 50}]
print(menu[1]["nombre"])  # Latte

# Ejemplo 3: Recorrido
for item in menu:
    print(f"{item['nombre']} - ${item['precio']}")
