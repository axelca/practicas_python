
def generar_acronimo(significado):
    palabras = significado.split()
    
    acronimo = ""
    
    for palabra in palabras:
        acronimo += palabra[0].upper()
    
    return acronimo

significado_completo = input("Por favor, ingresa el significado completo: ")

acrónimo = generar_acronimo(significado_completo)

print(f"Salida -> {significado_completo} -> {acrónimo}")
