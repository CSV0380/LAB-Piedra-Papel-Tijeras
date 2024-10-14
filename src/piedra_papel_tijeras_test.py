from piedra_papel_tijeras import *

def test_ordenador_decide_jugada():
    print("Testeando ordenador_decide_jugada...")
    eleccion = ordenador_decide_jugada()
    print("El ordenador eligió:", eleccion)
    print()

def test_usuario_decide_jugada():
    print("Testeando usuario_decide_jugada...")
    eleccion = usuario_decide_jugada()
    print("El usuario eligió:", eleccion)
    print()

def test_determina_ganador(eleccion_jugador, eleccion_ordenador):
    print("Testeando determina_ganador...")        
    print(f"Jugador: {eleccion_jugador} vs. Ordenador: {eleccion_ordenador}")
    resultado = determina_ganador(eleccion_jugador, eleccion_ordenador)
    print("Resultado:", resultado)
    print()






if __name__ == "__main__":
    #test_ordenador_decide_jugada()
    #test_usuario_decide_jugada()
    # jugada_mia = input("Decide tu jugada: ")
    # jugada_orde = ordenador_decide_jugada
    # test_determina_ganador(jugada_mia, jugada_orde)
    # test_determina_ganador("piedra", "tijeras")
    # jugar()
    rondas = int(input("Decide a cuántos puntos quieres jugar: "))
    jugar_torneo(rondas)
