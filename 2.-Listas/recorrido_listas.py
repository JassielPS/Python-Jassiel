# Ejemplo 1: for clásico
for cafe in cafes:
    print(f"☕ {cafe}")

# Ejemplo 2: enumerate()
for idx, cafe in enumerate(cafes):
    print(f"{idx + 1}. {cafe}")

# Ejemplo 3: List comprehension
precios_con_iva = [p * 1.16 for p in [45, 50, 60]]
print(precios_con_iva)
