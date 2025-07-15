# Ejemplo 1: if-elif-else
nota = 85
if nota >= 90:
    print("A")
elif nota >= 80:
    print("B")
elif nota >= 70:
    print("C")
else:
    print("F")

# Ejemplo 2: Múltiples condiciones
clima = "nublado"
if clima == "sol":
    print("Playa")
elif clima == "lluvia":
    print("Cine")
elif clima == "nublado":
    print("Montaña")
else:
    print("Quedarse en casa")

# Ejemplo 3: Combinando operadores
edad = 25
if edad < 18:
    print("Joven")
elif 18 <= edad < 65:
    print("Adulto")
else:
    print("Adulto mayor")
