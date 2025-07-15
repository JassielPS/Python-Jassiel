# Ejemplo 1: Diccionario anidado
menu = {
    "bebidas": {"calientes": ["Café", "Té"], "frías": ["Limonada"]},
    "precios": {"Café": 45, "Té": 30}
}
print(menu["bebidas"]["calientes"])

# Ejemplo 2: Modificar anidado
menu["precios"]["Café"] = 50
print("Nuevo precio:", menu["precios"]["Café"])

# Ejemplo 3: Recorrer
for categoria, items in menu["bebidas"].items():
    print(f"{categoria}: {items}")
