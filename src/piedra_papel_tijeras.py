import random

def ordenador_decide_jugada():
    opciones = ["piedra", "papel", "tijeras"]
    res = random.choice(opciones)
    return res



def usuario_decide_jugada():
    opciones = ["piedra", "papel", "tijeras"]
    eleccion = input("Elige entre piedra, papel o tijeras: ").lower() #sirve para que todo lo que ponags en el input se transforme a minuscula
    while eleccion not in opciones:
        eleccion = input("Opción no válida, por favor elige piedra, papel o tijeras: ").lower()
    return eleccion


def determina_ganador(jugada_usuario, jugada_ordenador):
    if jugada_usuario == jugada_ordenador:
        return "Empate"
    elif jugada_usuario == "piedra" and jugada_ordenador == "tijeras":
        return "Ganaste"
    elif jugada_usuario == "tijeras" and jugada_ordenador == "papel":
        return "Ganaste"
    elif  jugada_usuario == "papel" and jugada_ordenador == "piedra":
        return "Ganaste"
    else:
        return "Perdiste"
    

def jugar():
    print("Bienvenido al juego de Piedra, Papel o Tijeras!!\n")
    ordenador_elige = ordenador_decide_jugada()
    persona_elige = usuario_decide_jugada()
    print(f"La jugada elegida por el ordenador ha sido: {ordenador_elige}")
    print(f"La jugada elegida por usted ha sido: {persona_elige}")
    resultado = determina_ganador(persona_elige, ordenador_elige)
    print(f"\nResultado de la ronda: {resultado}")


def jugar_torneo(puntos):
    print(f"¡Bienvenido al torneo de Piedra, Papel o Tijeras a {puntos} puntos!")
    puntos_usuario = 0
    puntos_ordenador = 0  
    
    while puntos_usuario < puntos and puntos_ordenador < puntos: #mientras que los puntos esten ahi dentro se juega        
        jugada_ordenador = ordenador_decide_jugada()
        jugada_usuario = usuario_decide_jugada()            
        print(f"El ordenador ha elegido: {jugada_ordenador}")
            
        resultado = determina_ganador(jugada_usuario, jugada_ordenador)
        print(f"Resultado de la ronda: {resultado}")             
    
        #Contador de puntos:
        if resultado == "Ganaste":
            puntos_usuario += 1
            print(f"Tienes {puntos_usuario} puntos.")
        elif resultado == "Perdiste":
            puntos_ordenador += 1
            print(f"El ordenador tiene {puntos_ordenador} puntos.")
        else:
            print("Empate, nadie suma puntos.")
        
        print(f"Puntuación actual: Jugador {puntos_usuario} - Ordenador {puntos_ordenador}\n")

    if puntos_usuario == puntos:
                print("¡Felicidades! Has ganado el torneo.")
    else:
        print("El ordenador ha ganado el torneo, GG.")