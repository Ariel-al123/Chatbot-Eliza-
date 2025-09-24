import os
import sys
import time
import threading
import pygame
import random
import pyttsx3

def resource_path(relative_path):
    # Obtiene la ruta absoluta al recurso, funciona para desarrollo y para PyInstaller """
    try:
        # PyInstaller crea una carpeta temporal y almacena la ruta en _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

if os.name == 'nt':
    import msvcrt
else:
    import tty
    import termios

# Constantes para teclas
if os.name == 'nt':
    KEY_UP = b'H'
    KEY_DOWN = b'P'
    KEY_ENTER = b'\r'
else:
    KEY_UP = b'\x1b[A'
    KEY_DOWN = b'\x1b[B'
    KEY_ENTER = b'\r'

# Inicializar pygame para audio
pygame.mixer.init()

def play_sound(audio_file):
    if audio_file == 0: audio_file_name = "sonido.mp3"
    elif audio_file == 1: audio_file_name = "enter.mp3"
    elif audio_file == 2: audio_file_name = "teclado.mp3"
    try:
        pygame.mixer.music.load(resource_path(audio_file_name))
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
    else:
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1).encode()
            if ch == b'\x1b':
                ch += sys.stdin.read(2).encode()
            return ch
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_opcciones(options, selected_index):
    clear_screen()
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
            clear_screen()

            # Mostrar mensaje de selección con puntos suspensivos
            print(f"{mensajes_postseleccion[selected_index]} ", end='', flush=True)
            
            print("", end='', flush=True) 

            for _ in range(3):
                time.sleep(0.4)
                print(".", end='', flush=True)

            
            time.sleep(0.5)
            clear_screen()
            break
    
    return selected_index

def nombre_usuario():
    clear_screen()
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


respuestas_por_palabra_clave = {
    ("hola", "buenas", "hey", "qué tal"): [
        "Hola. Soy Eliza. Por favor, dime tu problema.",
        "Hola, ¿qué te trae por aquí?",
        "Hola, ¿cómo te sientes hoy?",
        "Un gusto saludarte, hablame sobre de ti."
    ],

    ("adiós", "hasta luego", "chao", "nos vemos"): [
        "Adiós. Gracias por hablar conmigo.",
        "Hasta luego, que tengas un buen día.",
        "Fue un placer conversar contigo. Adiós.",
        "Espero que podamos hablar de nuevo pronto."
    ],

    ("nombre", "me llamo", "soy"): [
        "Gracias por decirme tu nombre.",
        "Es un placer conocerte.",
        "¿Qué significa tu nombre?",
        "¿Siempre te ha gustado tu nombre?"
    ],
    
    ("necesito", "quiero", "me gustaría"): [
        "¿Por qué lo necesitas?",
        "¿Qué pasaría si no lo tuvieras?",
        "Entiendo que lo desees.",
        "¿Crees que obtenerlo te hará sentir mejor?"
    ],
  
    ("siento", "estoy", "me siento"): [
        "¿Por qué te sientes así?",
        "Lamento oír que te sientes así. Cuéntame más.",
        "Describe con más detalle ese sentimiento.",
        "¿Qué crees que provoca ese estado en ti?"
    ],

    ("recuerdo", "memoria"): [
        "¿Qué más recuerdas sobre eso?",
        "¿Cómo te hace sentir ese recuerdo?",
        "Los recuerdos son la clave del pasado.",
        "A veces los recuerdos nos enseñan más de lo que pensamos."
    ],

    ("madre", "mamá", "padre", "papá", "hermano", "hermana", "familia"): [
        "Háblame sobre tu familia.",
        "La familia es un tema importante. ¿Cómo te llevas con ellos?",
        "¿Crees que tu familia influye en cómo eres?",
        "A veces la familia nos marca más de lo que pensamos."
    ],

    ("eres", "sos", "tú"): [
        "¿Qué te hace pensar eso de mí?",
        "¿Realmente importa lo que soy? Hablemos de ti.",
        "Yo no soy lo importante aquí, tú lo eres.",
        "Parece que quieres saber más de mí, pero pero no importa, me gusta leer sobre ti."
    ],

    ("por qué", "porque", "razón"): [
        "Recuerda que no son lo hechos que nos afectan, sino la interpretacion sobre ellos son los que nos afectan.",
        "¿Por qué crees que es importante?",
        "A veces la razón no es tan clara como pensamos.",
        "En retrospectiva es facil ver los errores, pero en el pasado no tanto."
    ],

    ("feliz", "alegre", "contento"): [
        "Me alegra que te sientas así.",
        "Eso suena muy positivo. ¿Qué lo provoca?",
        "¿Cómo podrías mantener ese sentimiento?",
        "La felicidad es algo valioso, cuéntame más."
    ],

    ("triste", "deprimido", "solo", "cansado"): [
        "Lamento que te sientas así. ¿Quieres hablar más de eso?",
        "Estar triste puede ser difícil. ¿Qué lo causa?",
        "A veces compartir lo que sientes ayuda. ¿Quieres decirmelo?",
        "¿Cómo podrías cuidar de ti mismo en este momento?"
    ]
}

respuestas_genericas = [
    "Ya veo.",
    "Por favor, continúa.",
    "Cuentame mas.",
    "No te entendí bien, ¿Puedes darme más detalles?",
    "¿Qué es lo que piensas?",
    "Entiendo cómo te puedes sentir.",
    "Continúa, te escucho...",
    "Eso es interesante, dime más.",
    "Eres interesante, cuentame más.",
    "¿Por qué piensas así?",
    "Cuéntame más sobre eso."
]

cambio_pronombres = {
    "yo": "tú",
    "mi": "tu",
    "mis": "tus",
    "soy": "eres",
    "estoy": "estás",
    "me": "te",
    "mío": "tuyo",
    "conmigo": "contigo",
    "siento": "sientes",
    "quiero": "quieres"
    
}

def Imprimir(texto, voz):
    engine = pyttsx3.init()
    engine.setProperty('rate', 200)  # Velocidad del habla
    engine.setProperty('volume', 1)  # Volumen (0.0 a 1.0)
    engine.getProperty('voices')

    print("Eliza: ", end='', flush=True)
    if voz == 0:
        engine.say(texto)
    
    # Mostrar el texto con efecto "máquina de escribir" en la misma línea
    for ch in texto:
        # Imprime cada carácter sin salto de línea y fuerza el vaciado del buffer
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(0.05)
    print()  # Salto de línea al final
    
   
    engine.runAndWait()

def generar_respuesta(entrada_usuario):
    palabras_clave = ["hola", "buenas", "hey", "qué tal",
                "adiós", "adios", "hasta luego", "chao", "nos vemos",
                "nombre", "me llamo", "soy",
                "necesito", "quiero", "me gustaría",
                "siento", "estoy", "me siento",
                "recuerdo", "memoria",
                "madre", "mamá", "padre", "papá", "hermano", "hermana", "familia",
                "eres", "sos", "tú",
                "por qué", "porque", "razón",
                "feliz", "alegre", "contento",
                "triste", "deprimido", "solo", "cansado"
                ]
    # Convertimos la entrada a una lista de palabras en minúsculas.
    # Esto es un ejemplo de manipulación de cadenas (string) y creación de
    #listas (list)
    palabras = entrada_usuario.lower().split()
    
    # Usamos un bucle 'for' para iterar sobre nuestro diccionario de reglas.
    for grupo_claves, respuestas in respuestas_por_palabra_clave.items():
        # Usamos otro bucle 'for' anidado para revisar cada palabra clave en el grupo.
        for clave in grupo_claves:
        # El operador 'in' es una forma simple y poderosa de verificar pertenencia.

         if clave in palabras:
            # Si encontramos una palabra clave, seleccionamos una respuesta estandar.
            # El operador '%' (módulo) nos ayuda a tomar una decisión simple.
            if clave in palabras_clave and len(palabras) > 2:
            # Reflejamos la frase del usuario, cambiando los pronombres.
                frase_reflejada = []
                for palabras in palabras:
                    # Usamos .get() para buscar en el diccionario de pronombres
                    #si la palabra no esta, simplemente la usamos tal cual.
                    frase_reflejada.append(cambio_pronombres.get(palabras, palabras))
                    
                # Unimos la lista de palabras para formar una nueva oración y la devolvemos.
                
                return "¿Dices que " + " ".join(frase_reflejada) + "?"
            else:
                # Si no, simplemente elegimos una respuesta al azar de la lista
                return random.choice(respuestas)
                # Si el bucle 'for' termina sin encontrar ninguna palabra clave,
                # devolveremos una respueesta generica

    return random.choice(respuestas_genericas)
    

def eliza_chat(name_user, voz):
# Imprimimos un mensaje de bienvenida una sola vez.
    os.system('cls' if os.name == 'nt' else 'clear')
    mensaje = "Hola. Soy Eliza. Por favor habla conmigo (Escribe 'adiós' para salir"
    
    Imprimir(mensaje, voz)

    # Este es el bucle de control de flujo principal. Se ejecutará para siempre.
    while True:
        #input() es una función integrada de Python que detiene el programa y espera texto del usuario.
        entrada_usuario = input(f"{name_user}: ")
        #Usamos un condicional 'if' para comprobar si el usuario quiere
        #El operador 'or' nos permite verificar múltiples condiciones.
        if entrada_usuario.lower() == "adiós" or entrada_usuario.lower() == "adios" or entrada_usuario.lower() == "salir":
            mensaje = "Adiós. Gracias por hablar conmigo."
            Imprimir(mensaje, voz)
            #La declaración 'break' rompe el bucle 'while' y termina el programa.
            break
            #Si no salimos, llamamos a nuestra función principal para obtener una respuesta.
    
        respuesta = generar_respuesta(entrada_usuario)
        #f-string (cadena formateada) es una forma moderna y legible de insertar variables en texto.
        Imprimir(mensaje, voz)
        
        # INICIO DE LA EJECUCIÓN -
        # Para probar el chatbot en tu libreta, simplemente descomenta y ejecuta la siguiente línea.

            

if __name__ == "__main__":
   resultado = Menu_Voz()
   # Valor de Menu_Voz():
   # Activado = 0
   # Desactivado = 1
   print(f"Resultado de la selección: {resultado}")
   nombre = nombre_usuario()
   print(f"Nombre del usuario: {nombre}")
   
   eliza_chat(nombre, resultado)