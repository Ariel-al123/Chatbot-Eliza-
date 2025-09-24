import pyttsx3
import os
import time
import sys
import msvcrt  # Para getch() en Windows


# Obtener el ancho de la terminal
#ancho = os.get_terminal_size().columns

#engine = pyttsx3.init()
#engine.setProperty('rate', 150)  # Velocidad del habla
#engine.setProperty('volume', 1)  # Volumen (0.0 a 1.0)


# Get and print available voices
#voices = engine.getProperty('voices')


#mensaje = "Hola soy jake el perro y los voy a matar a todos"

#engine.say(mensaje)

#print(mensaje.center(ancho))
#engine.runAndWait()
    #print(f"Voice: {x.name}")
    #print(f" - ID: {x.id}")
    #print(f" - Languages: {x.languages


cad = "Facultad de ingenieria Mecanica Y Electrica"
print("Eliza : ", end='', flush=True)

for x in range(len(cad)):
    os.system('cls' if os.name == 'nt' else 'clear')
    for y in range(x + 1):
        print(cad[y], end='', flush=True)
    time.sleep(0.05)  # 50 milisegundos
    print()  # Nueva línea después de cada subcadena

msvcrt.getch() 
#  