import os
import time
import threading
import pygame
import clear



if os.name == 'nt':
    import msvcrt


# Constantes para teclas
if os.name == 'nt':
    KEY_UP = b'H'
    KEY_DOWN = b'P'
    KEY_ENTER = b'\r'


# Inicializar pygame para audio
pygame.mixer.init()

def play_sound(audio_file):
    if audio_file == 0: audio_file_name = "sonido.mp3"
    elif audio_file == 1: audio_file_name = "enter.mp3"
    elif audio_file == 2: audio_file_name = "teclado.mp3"
    try:
        pygame.mixer.music.load(audio_file_name)
        pygame.mixer.music.play()
        # Esperar a que termine la reproducción
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    except Exception as e:
        pass
def get_key():
    if os.name == 'nt':
        key = msvcrt.getch()
        if key == b'\xe0':
            key = msvcrt.getch()
        return key
    



def print_opcciones(options, selected_index):
    clear.clear_screen()
    print("=== Voz de Eliza ===\n")
    for i, option in enumerate(options):
        if i == selected_index:
            print(f"    {option} <")
        else:
            print(f"    {option}")
    print("\nUsa las flechas ↑/↓ y Enter para seleccionar")

def Menu_Voz():
    options = ["Voz Activada", "Voz Desactivada"]
    selected_index = 0
    last_index = 0  # Track del último índice seleccionado
    
    while True:
        print_opcciones(options, selected_index)
        
        # Reproducir sonido solo si hubo cambio de selección
        if selected_index != last_index:
            threading.Thread(target=play_sound, args=(0,)).start() # Sonido.mp3
            last_index = selected_index
            
        key = get_key()
        
        if key == KEY_UP and selected_index > 0: # Subir
            selected_index -= 1
        elif key == KEY_DOWN and selected_index < len(options) - 1: # Bajar
            selected_index += 1
        elif key == KEY_ENTER: # Enter
            threading.Thread(target=play_sound, args=(1,)).start() # Enter.mp3
           
            mensajes_postseleccion = [
                "Has activado la voz",
                "La voz está ahora desactivada"
            ]
            time.sleep(0.3)
            clear.clear_screen()

            # Mostrar mensaje de selección con puntos suspensivos
            #print(f"{mensajes_postseleccion[selected_index]} ", end='', flush=True)
            
            
            
            time.sleep(0.5)
            clear.clear_screen()
            break
    
    return selected_index

def nombre_usuario():
    clear.clear_screen()
    print("=== Nombre de Usuario ===\n")
    print("Por favor, ingresa tu nombre: ", end='', flush=True)
    nombre = ""
    while True:
        tecla = msvcrt.getch()  # Captura una tecla sin esperar Enter
        
        if tecla == b'\r':  # Enter para terminar
            print()
            if nombre == "":
                nombre = "User"
            break
        elif tecla == b'\x08':  # Backspace
            if len(nombre) > 0:
                nombre = nombre[:-1]
                print("\b \b", end="", flush=True)  # Borra el último carácter en pantalla
        else:
            try:
                char = tecla.decode("utf-8")
                nombre += char
                print(char, end="", flush=True)
                # Sonido cada vez que escribe una letra
                threading.Thread(target=play_sound, args=(2,)).start()  # Teclado.mp3 
                
            except UnicodeDecodeError:
                pass
                
    return nombre

def saldo():
    clear.clear_screen()
    print("=== Saldo Inicial ===\n")
    saldo = None
    try:
        saldo = int(input("Por favor, ingresa tu saldo inicial (número): "))
    except ValueError:
        saldo = 30000

    if saldo is None or saldo <= 0:
        saldo = 30000

    return saldo
      

if __name__ == "__main__":
   # Valor de Menu_Voz():
   # Activado = 0
   # Desactivado = 1
   
   resultado = Menu_Voz()
   nombre = nombre_usuario()
   Saldo = saldo()
    
   clear.clear_screen()

   print("Configuración completada. Iniciando Eliza...\n")
   print(f"Resultado de la selección: {resultado}")
   print(f"Nombre del usuario: {nombre}")
   print(f"Saldo inicial: {Saldo}")

   time.sleep(1)
   
   os.system(f"python eliza.py {nombre} {resultado} {Saldo}")