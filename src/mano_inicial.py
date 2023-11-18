"""Sacamos dos cartas para cada jugador como mano inicial."""
def primera_ronda(jugador: str) -> str:
    from sacar_carta        import draw_card
    from valor_por_carta    import valor_carta
    
    mano_jugador = ''
    
    for carta in range(2):

        mano_jugador = mano_jugador + draw_card()
        
    return mano_jugador

