#creamos una función para que asigna los valores a las figuras de la baraja y modifique a conveniencia el valor de A
def puntuacion_carta(carta: str) -> int:

    valor = 0
    
    #Actualizamos los valores str de las figuras a un valor numérico:
    if (carta == "J") or (carta == "K") or (carta == "Q") or (carta == "0"):
        valor = 10
        
    #Actualizamos el valor de A a 11. Durante el turno deberemos controlar la condición de cambiar a valor 1 o no.
    elif (carta == "A"):
        valor = 11
        
    #Si es cualquier otra carta de la baraja simplemente formateamos el tipo de dato para que mantenga su puntiación
    else:
        valor = int(carta)   
    
    #Devolvemos el valor numérico de la carta.
    return valor
