"""Nuestra función mano va a recibir los parámetros de: el nombre del jugador y el valor de una carta, que conformará la mano. 
De ésta manera iniciamos la mano con dos cartas y después usaremos la funcion obt_carta() para ir pidiendo en caso de querer más cartas."""
def mano_inicial(jugador: str) -> str:
    
    from dar_carta import obtener_carta
    #Generamos dos cartas, pero recibimos ya sus valores (por si ha tocado alguna figura) y asi calcular la puntuacion actual.
    carta1 = (obtener_carta())
    carta2 = (obtener_carta())
    valor_mano_inicial = (carta1) + (carta2)
    mano_jugador = f"El jugador {jugador} tiene como mano inicial: {carta1}, {carta2}"
    
    return valor_mano_inicial
