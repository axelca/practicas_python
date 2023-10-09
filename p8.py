# Función para verificar si una palabra es un palíndromo
def es_palindromo(palabra):
    palabra = palabra.lower()  # Convertir la palabra a minúsculas para hacer la comparación insensible a mayúsculas
    return palabra == palabra[::-1]  # Comprobar si la palabra es igual a su reverso

# Solicitar al usuario cinco palabras
palabras = []
for i in range(5):
    palabra = input(f"Ingrese la palabra {i+1}: ")
    palabras.append(palabra)

# Verificar si alguna de las palabras es un palíndromo
palindromos = [palabra for palabra in palabras if es_palindromo(palabra)]

# Mostrar el resultado
if len(palindromos) > 0:
    print("Las siguientes palabras son palíndromos:")
    for palindromo in palindromos:
        print(f"- {palindromo}")
else:
    print("Ninguna de las palabras ingresadas es un palíndromo.")
