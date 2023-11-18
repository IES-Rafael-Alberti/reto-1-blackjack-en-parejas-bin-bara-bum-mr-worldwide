def nombre_jugadores(mod_juego: int) -> str:
    from clr_term           import clear_terminal
    
    clear_terminal()
    
    try: 
        
        if (mod_juego == 1):
            print('Has elegido el modo de juego Jugador contra Jugador')
            jugador_1 = input('Jugador 1, introduce tu nombre: ').title()
            jugador_2 = input('Jugador 2, introduce tu nombre: ').title()
            print(f'*** {jugador_1} VS {jugador_2} ***')
        
        elif (mod_juego == 2):
            
            print('Vas a jugar contra la maquina')
            jugador_1 = input('Jugador 1, introduce tu nombre: ').title()
            jugador_2 = 'Maquitron'
            print(f'*** {jugador_1} VS {jugador_2} ***')
            
        if (jugador_2 == None):
            raise Exception('El modo de juego debe ser 1 o 2')
        
        jugadores = jugador_1, jugador_2
        
        return jugadores
    
    except Exception as e:
        return str(e)