def play_mod() -> int:

    try:
        
        print('Elige un modo de juego introduciendo el numero de la opcion:\n1.- Jugador contra Jugador.\n2.- Jugador contra Maquina')
        mod_juego = input()
        
        mod_juego = int(mod_juego)
        
        if mod_juego in range(1,3):
            return mod_juego
        
        else:
            raise ValueError('Debes introducir una de las opciones.')
        
    except ValueError:
        return ('Debes introducir una de las opciones.')

