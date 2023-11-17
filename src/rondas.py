def ronda(jugador: str, seguir: str):
    from dar_carta import obtener_carta
    from valor_carta import puntuacion_carta
    try:
        
        if (seguir.lower() == "si"):
            otra_carta = puntuacion_carta(obtener_carta)
            return otra_carta
        else:
            print(f"{jugador} se planta.")
            
    except ValueError:
        print("Indica si quieres seguir con [si] o [no]: ")    
    