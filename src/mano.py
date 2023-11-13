"""Nuestra función mano va a recibir los parámetros de: el nombre del jugador y el valor de una carta, que conformará la mano. 
De ésta manera iniciamos la mano con dos cartas y después usaremos la funcion obt_carta() para ir pidiendo en caso de querer más cartas."""
def mano_inicial(jugador: str) -> str:
    
    from obt_carta import obtener_carta
    from valor_carta import puntuacion_carta
    #Generamos dos cartas, pero recibimos ya sus valores (por si ha tocado alguna figura) y asi calcular la puntuacion actual.
    carta1 = puntuacion_carta(obtener_carta())
    carta2 = puntuacion_carta(obtener_carta())
    
    mano_jugador = f"El jugador {jugador} tiene como mano inicial: {carta1}, {carta2}"
    
    #Sumamos el valor de las cartas para mostras la puntuacion de la mano inicial.

    return mano_jugador
    
    
"""sum_cartas = carta1 + carta2
puntuacion = f"Puntuacion actual: {sum_cartas}"

resultado = f"{mano_jugador}\n{puntuacion}""" 
