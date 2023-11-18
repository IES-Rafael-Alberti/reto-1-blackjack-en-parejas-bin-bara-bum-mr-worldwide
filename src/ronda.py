"""Vamos a generar una ronda generica que se vaya repitiendo, mientras al menos uno de los jugadores quiera plantarse recibiendo cartas"""
def round(nombre_jugador: str) -> str:
    from sacar_carta import draw_card
    
    plantarse = 'NO'
    
    while (plantarse == 'NO'):
        
        carta = draw_card()
        
        plantarse = input(f'{nombre_jugador}, quieres otra carta?: ').upper()
        
        if (plantarse == 'SI'):
            plantarse = 'SI'
            
        return carta
    
print(round('sara'))