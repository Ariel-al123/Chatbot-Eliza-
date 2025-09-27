import os

# Obtener el ancho de la terminal
def Menu():
    ancho = os.get_terminal_size().columns    
  
    mensaje = "Adios    |   Salir de Programa   "
    print(mensaje.rjust(ancho))
    
    mensaje = "Caro     |   Opcción de Objetar  "
    print(mensaje.rjust(ancho))

    mensaje = "Colocar  |   Añadir al Carrito   "
    print(mensaje.rjust(ancho))

    mensaje = "Carrito  |   Observar Carrito    "
    print(mensaje.rjust(ancho))

    mensaje = "Comprar  |   Comprar Carrito     "
    print(mensaje.rjust(ancho))

