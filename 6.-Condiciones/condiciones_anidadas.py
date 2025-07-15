# Ejemplo 1: Anidado simple
usuario = "admin"
clave = "1234"
if usuario == "admin":
    if clave == "1234":
        print("Acceso concedido")
    else:
        print("Clave incorrecta")
else:
    print("Usuario incorrecto")

# Ejemplo 2: Anidado con operadores lógicos
numero = 15
if numero > 0:
    if numero < 10:
        print("Dígito")
    else:
        print("Número positivo de dos o más dígitos")
else:
    print("Número no positivo")

# Ejemplo 3: Mezcla con lógicos
puntos = 85
if puntos >= 50:
    if puntos >= 75:
        print("Aprobado con excelencia")
    else:
        print("Aprobado")
else:
    print("Reprobado")
