"""Funcion principal para un juego de Black Jack.
Cargaremos las distintas funciones que iremos usando para ayudarnos a lo largo del proceso del jeugo."""
"""
#Importacion de funciones que vamos a usar 
import time 
from bienvenida         import bienvenidos
from clr_term           import clear_terminal
from modo_juego         import play_mod
from jugadores          import nombre_jugadores
from mano_inicial       import primera_ronda
from puntos_por_carta   import valor_cartas_manos

#Funcion principal
def main():
    clear_terminal()
    print(bienvenidos())
    
    try:
        #Variables que vamos a usar en la funcion main
        #Contador de rondas 
        ronda = 1
        
        #Indicamos el tipo de juego
        tipo_juego = play_mod()
        #Definimos el segundo jugador teniendo en cuenta la modalidad de juego y el nombre del primer jugador 
        jugadores = nombre_jugadores(tipo_juego)
        
        time.sleep(2)
        
        #Iniciamos la partida repartiendo dos cartas a cada jugador en la Ronda 1
        while (ronda == 1):
            clear_terminal()
            print(f'_==RONDA {ronda}==_\n')
            jugador_1 = ''
            jugador_2 = ''
            for participante in jugadores[0]:
                jugador_1 = jugador_1 + participante
            for participante in jugadores[1]:
                jugador_2 = jugador_2 + participante
                
            #Vamos iniciando la mano de cada jugador
            mano_jugador_1 = primera_ronda(jugador_1)
            mano_jugador_2 = primera_ronda(jugador_2)
            #Mostramos los resultados de la mano inicial para que los jugadores decidan si quieren continuar o no.
            j1 = f'J1 - {jugador_1} - {mano_jugador_1} ({valor_cartas_manos(mano_jugador_1)})'
            j2 = f'J2 - {jugador_2} - {mano_jugador_2} ({valor_cartas_manos(mano_jugador_2)})'
            
            print (j1)
            print (j2)
            
            ronda += 1
            
            continuar_j1 = input(f'{jugador_1} quieres continuar?')
            continuar_j2 = input(f'{jugador_1} quieres continuar?')
            
    except Exception:
        print('Ocurrió un error inesperado en el programa.')
        
    
    
if __name__=="__main__":
    main()
"""