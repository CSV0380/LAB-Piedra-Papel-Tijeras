from piedra_papel_tijeras import *



def test_ordenador_decide_jugada():
    print("Testeando que el ordenador decide una jugada...")
    resultado = ordenador_decide_jugada()
    print("El ordenador ha elegido: " + resultado)




if __name__ == "__main__":
    test_ordenador_decide_jugada()
    