"""Funcion principal para un juego de Black Jack.
Cargaremos las distintas funciones que iremos usando para ayudarnos a lo largo del proceso del jeugo."""

#Importacion de funciones que vamos a usar 
import time 
from bienvenida         import bienvenidos
from clr_term           import clear_terminal
from modo_juego         import play_mod
from jugadores          import nombre_jugadores
from mano_inicial       import primera_ronda
from puntos_por_carta   import valor_cartas_manos
from sacar_carta        import draw_card


#Funcion principal
def main():
    clear_terminal()
    print(bienvenidos())
    try:
        """Variables que vamos a usar en la funcion main"""
        #Contador de rondas 
        ronda = 1
        #Pedimos el nombre al jugador 1
        #jugador_1 = input('Hola Jugador 1, introduce tu nombre: ').title()
        
        #Indicamos el tipo de juego
        tipo_juego = play_mod()
        #Definimos el segundo jugador teniendo en cuenta la modalidad de juego y el nombre del primer jugador 
        jugadores = nombre_jugadores(tipo_juego)
        jugador_1 = jugadores[0]
        jugador_2 = jugadores[1]
        time.sleep(2)
        
        #Iniciamos la partida repartiendo dos cartas a cada jugador en la Ronda 1
        #PRIMERA RONDA, cada jugador recibe obligatoriamente dos cartas
        print(f'_==RONDA {ronda}==_\n')
        print(f'{jugador_1} VS {jugador_2}')
        
        #Vamos iniciando la mano de cada jugador
        mano_jugador_1 = primera_ronda(jugador_1)
        mano_jugador_2 = primera_ronda(jugador_2)
        
        #Mostramos los resultados de la mano inicial para que los jugadores decidan si quieren continuar o no.
        j1 = f'J1 - {jugador_1} - {mano_jugador_1} ({valor_cartas_manos(mano_jugador_1)})'
        j2 = f'J2 - {jugador_2} - {mano_jugador_2} ({valor_cartas_manos(mano_jugador_2)})'
        
        #Mostramos las manos iniciales de los jugadores 
        print (j1)
        print (j2)
        
        #Tras la primera ronda, viendo el restultado obtenido en las cartas, los jugadores pueden decirdir si plantarse o seguir recibiendo cartas
        seguir_j1 = input(f'{jugador_1}, quieres plantarte?[si/no]: ')
        seguir_j2 = input(f'{jugador_2}, quieres plantarte?[si/no]: ')
        
        

            
    except Exception:
        print('Ocurrió un error inesperado en el programa.')
        
    
    
if __name__=="__main__":
    main()