"""Vamos a sacar un mensaje de cabecera"""


def bienvenidos() -> str:
    
    linea1 = '***********************************'
    centro = len(linea1)
    bienvenida = ('BIENVENIDOS AL GRAN').center(centro)
    black_jack = 'BLACK JACK'.center(centro)

    mensaje = (f'\n{linea1}\n{bienvenida}\n{black_jack}\n{linea1}\n\n')

    return mensaje
print (bienvenidos())