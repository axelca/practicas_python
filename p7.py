import random

def jugar_adivina_el_numero():
    numero_secreto = random.randint(1, 50)
    intentos = 0
    
    print("¡Bienvenido al juego de Adivina el número!")
    
    while True:
        intento = input("Adivina un número entre 1 y 50: ")
        
        if intento.lower() == "salir":
            print(f"El número secreto era {numero_secreto}. ¡Hasta luego!")
            break
        
        if not intento.isdigit():
            print("Por favor, ingresa un número válido.")
            continue
        
        intento = int(intento)
        
        if intento < 1 or intento > 50:
            print("Por favor, ingresa un número dentro del rango adecuado (entre 1 y 50).")
            continue
        
        intentos += 1
        
        if intento < numero_secreto:
            print("Intenta un número más alto.")
        elif intento > numero_secreto:
            print("Intenta un número más bajo.")
        else:
            print(f"¡Felicidades! Adivinaste el número secreto ({numero_secreto}) en {intentos} intentos.")
            break

jugar_adivina_el_numero()
