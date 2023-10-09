
nombre = input("¿Cómo te llamas? ")
fecha_de_nacimiento = input("¿Cuál es tu fecha de nacimiento (por ejemplo, Jan 1, 1954)? ")
direccion = input("¿Cuál es tu dirección? ")
metas_personales = input("¿Cuáles son tus metas personales? ")

if nombre.strip() == "":
    print("Error: Debes ingresar un nombre válido.")
elif fecha_de_nacimiento.strip() == "":
    print("Error: Debes ingresar una fecha de nacimiento válida.")
elif direccion.strip() == "":
    print("Error: Debes ingresar una dirección válida.")
elif metas_personales.strip() == "":
    print("Error: Debes ingresar metas personales válidas.")
else:
    print("\nResumen de la información:")
    print(f"- Nombre: {nombre}")
    print(f"- Fecha de nacimiento: {fecha_de_nacimiento}")
    print(f"- Dirección: {direccion}")
    print(f"- Metas personales: {metas_personales}")
