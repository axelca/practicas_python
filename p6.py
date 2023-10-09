def determinar_ganador(eleccion_usuario, eleccion_computadora):
    if eleccion_usuario == eleccion_computadora:
        return "Empate"
    elif (eleccion_usuario == "Piedra" and eleccion_computadora == "Tijeras") or \
         (eleccion_usuario == "Papel" and eleccion_computadora == "Piedra") or \
         (eleccion_usuario == "Tijeras" and eleccion_computadora == "Papel"):
        return "¡Ganaste!"
    else:
        return "La computadora ganó."

def jugar_piedra_papel_tijeras():
    print("Bienvenido al juego de Piedra, Papel, Tijeras")
    eleccion_usuario = input("Elige Piedra, Papel o Tijeras: ").capitalize()
    
    if eleccion_usuario not in ["Piedra", "Papel", "Tijeras"]:
        print("Opción no válida. Por favor, elige entre Piedra, Papel o Tijeras.")
        return
    
    eleccion_comp = input("La computadora elige: ").capitalize()
    print(f"La computadora eligió: {eleccion_comp}")
    
    resultado = determinar_ganador(eleccion_usuario, eleccion_comp)
    print(resultado)

jugar_piedra_papel_tijeras()