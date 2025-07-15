# Ejemplo 1: filter()
caros = list(filter(lambda p: p > 50, [45, 50, 60]))
print(f"Precios caros: {caros}")

# Ejemplo 2: map()
precios_str = list(map(str, [45, 50, 60]))
print(f"Como strings: {precios_str}")

# Ejemplo 3: slice()
primero = cafes[:1]
ultimos = cafes[-2:]
print(f"Primero: {primero}, Últimos: {ultimos}")
