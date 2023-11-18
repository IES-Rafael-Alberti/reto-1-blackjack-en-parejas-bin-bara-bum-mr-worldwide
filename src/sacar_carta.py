"""Creamos una funcion que nos sacara cartas aleatorias de nuestra baraja."""
def draw_card() -> str:
    import random
    
    baraja = 'A234567890JKQ'
    
    carta = random.choice(baraja)
    
    return carta
    