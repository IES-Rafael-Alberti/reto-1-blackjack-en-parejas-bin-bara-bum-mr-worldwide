#Función que nos dará una carta de forma aleatoria, dentro de la baraja.
def obtener_carta() -> int:
    
    #Vamos a sacar una carta al azar con la funcion random.
    import random 
    baraja = "A234567890JKQ"
    carta = random.choice(baraja)
    
    #Devolvemos como valor la carta generada.
    return carta     