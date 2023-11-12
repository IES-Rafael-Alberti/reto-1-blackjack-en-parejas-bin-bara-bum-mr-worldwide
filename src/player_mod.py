"""
Funcion que determinará si se va a jugar PVP o jugador contra la máquina.
Sólo obtendremos el nombre del segundo jugador, según modo de juego.
El nombre de Jugador_1 lo vamos a obtener en la funcion main()
"""

def modo_juego(option_player: int):
    
    if (option_player == 1):
        print("Introduce el nombre del jugador 2: ")
        nom_jugador_2 = input()
        
    elif (option_player == 2):
        nom_jugador_2 = "Maquitrón"
        
    else:
        
        raise ValueError ("**ERROR**\nDebes indicar opción 1 o 2.")
    
    return nom_jugador_2



def main():
    
    try:
        print("Introduce tu nombre: ")    
        jugador_1 = input()
        
        print(f"{jugador_1}, indica cómo deseas jugar [1 o 2]:\n1.- Jugador Versus Jugador\n2.-Jugador contra la máquina")
        
        option_player =int(input())
        if (option_player == 1): 
            jugador_2 = modo_juego(option_player)
            print(f"Has elegido el modo de juego: jugador contra jugador.\n{jugador_1} VS {jugador_2}")
            
        elif (option_player == 2): 
            jugador_2 = modo_juego(option_player)
            print(f"Has elegido jugar contra la máquina.\n{jugador_1} VS {jugador_2}")
            
    except ValueError as e:
        print(e)
        
        
if __name__=="__main__":
    main()