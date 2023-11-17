def total_puntos(cartas: str) -> int:
    
    from valor_carta import puntuacion_carta
    
    #RECORREMOS LA LISTA DE LAS CARTAS Y LAS SUMAMOS COMO VALORES NUMERICOS 
    puntos_totales = 0
    for carta in cartas:
        puntos_totales += puntuacion_carta(carta)
        
    if ('A' in cartas) and (puntos_totales >= 21):
        
        puntos_totales -= 10
        
    #DEVOLVEMOS LA PUNTUACION FINAL DE TODAS LAS CARTAS 
    return puntos_totales
