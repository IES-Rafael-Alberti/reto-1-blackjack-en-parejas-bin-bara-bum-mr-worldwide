"""Vamos a asignar valores numericos a las cartas que vayamos sacando."""
def valor_carta(carta: str) -> int:
    try:
        #Inicializamos el valor de la carta en 0 
        puntos_carta = 0
        #Las figuras tendran un valor de 10
        figuras = 'AJKQ0'
        
        
        if carta in figuras:
            if carta == 'A':
                #El As tiene una puntuacion base de 11, que cambiaria a 1 segun el resto de cartas de la mano, lo controlaremos en la funcion que calcule la puntuacion total de la mano, en favor del jugador.
                puntos_carta = 11
            else:
                #El resto de figuras tiene asignado el valor de 10 
                puntos_carta = 10
                
        else:
            #Si la carta no es una figura, su puntuacion sera igual al numero que representado con el caracter tipo str.
            puntos_carta = int(carta)

        #Devolvemos el valor numerico de la carta.
        return puntos_carta

    except Exception:
        return('ERROR - 404')