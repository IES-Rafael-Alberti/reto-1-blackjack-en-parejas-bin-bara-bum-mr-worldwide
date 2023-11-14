#####hoze, aqui vamos a meter el main para q vaya llamando a las otras funciones

def jugar_black_Jack():
    
    #Importamos todas las funciones que vamos a necesitar para el desarrollo del juego:
    from src.eleccion_jugador import modo_juego
    from src.iniciar_mano import mano_inicial
    from src.obt_carta import obtener_carta
    from src.valor_carta import puntuacion_carta
    from src.total_puntos_cartas import total_puntos
    #//////////////////////////\\\\\\\\\\\\\\\\\\\\\\\#
    try:
        #####PRINT MENSAJE DE BIENVENIDA#####
        
        #INICIO DEL JUEGO
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
        
        lista_jugadores = jugador_1, jugador_2
        
        #INICIALIZAR LA MANO 
        #Iniciamos la partida repartiendo dos cartas por jugador. 
        #---JUGADOR1---#
        """ESTOY HAY QUE PONERLO BONITO"""
        cartas_jugador1 = ""
        mano_ini_j1 = mano_inicial(jugador_1)
        otra_carta_j1 = obtener_carta()
        
        #LISTA DE LAS CARTAS
        cartas_jugador1 = str(cartas_jugador1) + str(mano_ini_j1) + str(otra_carta_j1)
        #PUNTUACION QUE SUMAN LAS CARTAS
        total_puntos(cartas_jugador1)
        
        


        
        
        
        """      
        cartas_jugador2 = ""
        mano_ini_j2 = (mano_inicial(jugador_2))
        otra_carta_j2 = (obtener_carta)
        cartas_jugador2 = cartas_jugador2 + mano_ini_j2 + otra_carta_j2
        print(cartas_jugador1)
        print (cartas_jugador1)
        """
        
        
        
        #---HAY QUE MOSTRAR LA MANO A CADA JUGADOR Y SE DA OBLIGATORIAMENTE 1 CARTA MAS ANTES DE QUE SE PUEDAN PLANTAR, DESPUES OPCIONAL POR RONDA---#
        
        #RONDAS
            #---REGUNTAR SI QUIEREN MAS CARTAS O SE PLANTAN---#
            #---HAY QUE INCLUIR LA PUNTUACION DE LA MANO INICIAL---#
            #RESULTADOS RONDA
            #CALCULAR RESULTADOS
        
        #CALCULAR GANADOR/EMPATE
        
    except ValueError as e:
        print(e)


jugar_black_Jack()