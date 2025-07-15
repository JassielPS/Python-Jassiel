# Ejemplo 1: update()
cliente.update({"edad": 27, "ciudad": "Cancún"})
print(cliente)

# Ejemplo 2: pop()
ciudad = cliente.pop("ciudad")
print(f"Ciudad removida: {ciudad}")

# Ejemplo 3: clear()
cliente.clear()
print("Diccionario vacío:", cliente)
