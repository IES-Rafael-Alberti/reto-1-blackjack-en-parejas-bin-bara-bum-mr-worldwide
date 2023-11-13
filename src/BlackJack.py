#####hoze, aqui vamos a meter el main para q vaya llamando a las otras funciones

def jugar_black_Jack():
    
    #Importamos todas las funciones que vamos a necesitar para el desarrollo del juego:
    from src.eleccion_jugador import modo_juego
    from src.obt_carta import obtener_carta
    from src.valor_carta import puntuacion_carta

    try:
        #####PRINT MENSAJE DE BIENVENIDA
        #Iniciación del juego
        print("Introduce tu nombre: ")    
        jugador_1 = input()
        
        #Pedimos el modo de juego: 
        print(f"{jugador_1}, indica cómo deseas jugar [1 o 2]:\n1.- Jugador Versus Jugador\n2.-Jugador contra la máquina")
        option_player =int(input())
        #PVP
        if (option_player == 1): 
            jugador_2 = modo_juego(option_player)
            print(f"Has elegido el modo de juego: jugador contra jugador.\n*****{jugador_1} VS {jugador_2}*****")
        #PVE
        elif (option_player == 2): 
            jugador_2 = modo_juego(option_player)
            print(f"Has elegido jugar contra la máquina.\n*****{jugador_1} VS {jugador_2}*****")
            
        else:
            raise ValueError ("**ERROR**\nDebes introducir una de las dos opciones.")
        
        #INICIALIZAR LA MANO 
            #INICIALIZAR PARA CADA JUGADOR 
            
        #AGREGAR CARTAS A LA MANO INICIAL     
                  
        #RONDAS
            #RESULTADOS RONDA
            #CALCULAR RESULTADOS
        
        #CALCULAR GANADOR/EMPATE
        
    except ValueError as e:
        print(e)


jugar_black_Jack()