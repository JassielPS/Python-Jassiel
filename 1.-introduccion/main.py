def mostrar_menu():
    print("☕ CoffeeTech")
    print("1. Espresso\n2. Capuchino\n3. Salir")
    opcion = input("Opción: ")
    if opcion == "1": print("🖤 Espresso...XD")
    elif opcion == "2": print("🍵 Capuchino...XD")
    elif opcion == "3": print("👋 Adiós")
    else: print("❌ Inválido...XD")

if __name__ == "__main__":
    mostrar_menu()
