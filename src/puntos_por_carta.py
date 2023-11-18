"""Vamos a calcular el valor de las cartas en mano."""
def valor_cartas_manos(mano: str) -> int:
    from valor_por_carta import valor_carta
    
    #Inicializamos la puntuacion de la mano en 0 
    puntos_mano = 0
    
    for carta in mano:
        puntos_mano += valor_carta(carta)
    #Controlamos la condicion que hace a A cambiar su valor numerico en favor del jugador, intercambiando al segundo valor posible.
    if ('A' in mano) and (puntos_mano > 21):
        puntos_mano -= 10
    
    return puntos_mano
    
