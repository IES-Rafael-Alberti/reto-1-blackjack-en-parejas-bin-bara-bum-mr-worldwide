"""Vamos a determinar el resultado de las manos jugadas."""
def resultado(jugador1: str, mano_j1: str, puntos_mano_j1: int, jugador2: str, mano_j2: str, puntos_mano_j2: int, ronda: int) -> str:
    
    try:
        j1 = f'J1 - {jugador1} - {mano_j1} - ({puntos_mano_j1})'
        j2 = f'J1 - {jugador2} - {mano_j2} - ({puntos_mano_j2})'
        
        #Mensaje si gana jugador 1:
        if (puntos_mano_j1 > puntos_mano_j2):
            return  (f'JUEGO TERMINADO - RONDA {ronda}\n¡Gana J1 - {jugador1}!\n{j1}\n{j2}')
        
        #Mensaje si gana jugador 2:
        elif (puntos_mano_j1 < puntos_mano_j2):
            return  (f'JUEGO TERMINADO - RONDA {ronda}\n¡Gana J2 - {jugador2}!\n{j1}\n{j2}')
        
        #Mensaje si hay empate:
        elif (puntos_mano_j1 == puntos_mano_j2):
            return  (f'JUEGO TERMINADO - RONDA {ronda}\n¡Empate!\n{j1}\n{j2}')
        
        #Mesaje si ambos jugadores pierden:
        elif (puntos_mano_j1 > 21) and (puntos_mano_j2 > 21):
            return  (f'JUEGO TERMINADO - RONDA {ronda}\nGame over ¡Los dos os habéis pasado!\n{j1}\n{j2}')
        
        
    except Exception:
        return('ERROR - 404')