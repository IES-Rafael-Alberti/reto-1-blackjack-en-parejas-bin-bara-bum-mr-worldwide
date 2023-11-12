"""
Funcion que determinará si se va a jugar PVP o jugador contra la máquina.
Sólo obtendremos el nombre del segundo jugador, según modo de juego.
El nombre de Jugador_1 lo vamos a obtener en la funcion main()
"""
def modo_juego(option_player: int):
    
    if (option_player == 1):
        print("Introduce el nombre del jugador 2: ")
        nom_jugador_2 = input()
        return nom_jugador_2

    elif (option_player == 2):
        nom_jugador_2 = "Maquitrón"
        return nom_jugador_2
    else:
        
        raise ValueError ("**ERROR**\nDebes indicar opción 1 o 2.")