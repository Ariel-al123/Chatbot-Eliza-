import random
import time
import sys
import pyttsx3
import os
# crear archivo de catalogo
# crea funciones donde se guarden las carcteristicas tecnicas en un archivo
# otro en donde se guarde la recomendacion anterior 

def Hacer_Carrito(objetos):
    archivo = open("carrito.txt", "w")

    for elemento in objetos:
        archivo.write(elemento + "\n")


def Leer_Carrito():
    archivo = open("carrito.txt", "r")

    contenido = archivo.read()
    print(contenido)


def Catalogo():
    archivo = open("carrito.txt", "r")

    contenido = archivo.read()
    print(contenido)

def Menu():
    ancho = os.get_terminal_size().columns    
  
    mensaje = "Adios    |   Salir de Programa   "
    print(mensaje.rjust(ancho))
    
    mensaje = "Catalogo |   Observar Catalogo   "
    print(mensaje.rjust(ancho))
    
    mensaje = "Caro     |   Opcción de Objetar  "
    print(mensaje.rjust(ancho))

    mensaje = "Colocar  |   Añadir al Carrito   "
    print(mensaje.rjust(ancho))

    mensaje = "Carrito  |   Observar Carrito    "
    print(mensaje.rjust(ancho))

    mensaje = "Comprar  |   Comprar Carrito     "
    print(mensaje.rjust(ancho))

respuestas_por_palabra_clave = {
    ("hola", "buenas", "hey", "qué tal"): [
        "Hola. Soy Eliza. Por favor, ¿En que puedo ayudate?.",
        "Hola, ¿En que puedo ayudate?",
        "Un gusto saludarte, hablame sobre de ti."
    ],

    ("nombre", "me llamo", "soy"): [
        "Gracias por decirme tu nombre.",
        "Es un placer conocerte."
    ],
    
  
    ("siento", "estoy", "me siento"): [
        "Lamento oír que te sientes así. Cuéntame más.",
        "¿Qué crees que provoca ese estado en ti?"
    ],

    ("recuerdo", "memoria"): [
        "¿Qué más recuerdas sobre eso?",
    ],

    ("madre", "mamá", "padre", "papá", "hermano", "hermana", "familia"): [
        "Háblame sobre tu familia.",
        "La familia es un tema importante. ¿Cómo te llevas con ellos?",
        "¿Crees que tu familia influye en cómo eres?",
        "A veces la familia nos marca más de lo que pensamos."
    ],

    ("eres", "sos", "tú"): [
        "¿Realmente importa lo que soy? Hablemos de ti.",
        "Yo no soy lo importante aquí, en que puedo ayudarte?.",
    ],

    ("feliz", "alegre", "contento"): [
        "Me alegra que te sientas así.",
        "Eso suena muy positivo. ¿Qué lo provoca?",
        "¿Cómo podrías mantener ese sentimiento?",
        "La felicidad es algo valioso, cuéntame más."
    ],
   
}


catalogo_productos_pc_todo = {
    "laptops": [
        {
            "nombre": "laptop1",
            "precio": 15000.00,
            "caracteristicas": [
                "16GB RAM", "RTX 3060", "SSD 512GB",
                "Intel i7 11ª Gen", "144Hz"
            ],
            "palabras_clave": (
                "laptop", "gaming", "juegos", "notebook",
                "pc", "portátil", "ordenador", "3060",
                "RTX", "intel", "gamer"
            ),
            "descuento_maximo": 0.15
        },
        {
            "nombre": "laptop2",
            "precio": 12000.00,
            "caracteristicas": [
                "8GB RAM", "Intel i5 12ª Gen",
                "SSD 256GB", "Pantalla 14'' FHD", "Ligera"
            ],
            "palabras_clave": (
                "laptop", "ultrabook", "ligera",
                "notebook", "trabajo", "portátil", "oficina"
            ),
            "descuento_maximo": 0.10
        },
        {
            "nombre": "laptop3",
            "precio": 25000.00,
            "caracteristicas": [
                "32GB RAM", "RTX 4070", "SSD 1TB",
                "Intel i9 13ª Gen", "Pantalla 16'' QHD 240Hz"
            ],
            "palabras_clave": (
                "laptop", "gaming", "profesional", "nvidia",
                "4070", "intel", "creadores", "render", "edición"
            ),
            "descuento_maximo": 0.20
        }
    ],

    "pc_escritorio": [
        {
            "nombre": "pc1",
            "precio": 8000.00,
            "caracteristicas": [
                "8GB RAM", "Ryzen 5 5600G",
                "SSD 480GB", "Gráficos integrados Vega"
            ],
            "palabras_clave": (
                "pc", "escritorio", "ordenador",
                "oficina", "básico", "amd", "trabajo"
            ),
            "descuento_maximo": 0.08
        },
        {
            "nombre": "pc2",
            "precio": 20000.00,
            "caracteristicas": [
                "16GB RAM", "RTX 3060 Ti",
                "SSD 1TB", "Ryzen 7 5800X"
            ],
            "palabras_clave": (
                "pc", "gaming", "nvidia", "ryzen",
                "juegos", "gamer", "desempeño"
            ),
            "descuento_maximo": 0.18
        },
        {
            "nombre": "pc3",
            "precio": 35000.00,
            "caracteristicas": [
                "64GB RAM", "RTX 4090",
                "SSD 2TB NVMe", "Intel Xeon",
                "Placa base workstation"
            ],
            "palabras_clave": (
                "pc", "workstation", "profesional", "render",
                "edición", "servidor", "intel", "4090", "nvidia"
            ),
            "descuento_maximo": 0.25
        }
    ]
}


respuestas_genericas = [
    "Ya veo.",
    "Por favor, continúa.",
    "Cuentame mas.",
    "No te entendí bien, ¿Puedes darme más detalles?",
    "Entiendo cómo te puedes sentir.",
    "Continúa, te escucho...",
    
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
    
    Menu()
    print("Eliza: ", end='', flush=True)
    if voz == 0:
        engine.say(texto)
    
    # Mostrar el texto con efecto "máquina de escribir" en la misma línea

    #print("")

    for ch in texto:
        # Imprime cada carácter sin salto de línea y fuerza el vaciado del buffer
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(0.05)
    print()  # Salto de línea al final
    
   
    engine.runAndWait()


def generar_respuesta(entrada_usuario):

    #Re hacer toda la funcion
    palabras_clave = ["hola", "buenas", "hey", "qué tal",
                "nombre", "me llamo", "soy",
                "siento", "estoy", "me siento",
                "recuerdo", "memoria",
                "madre", "mamá", "padre", "papá", "hermano", "hermana", "familia",
                "eres", "sos", "tú",
                "feliz", "alegre", "contento",
    ]
    acciones_claves = {
        "adios", "adiós",
        "catalogo", "catálogo"
        "caró", "caro",
        "colocar", "carrito",
        "comprar"
    }

    # Convertimos la entrada a una lista de palabras en minúsculas y las separamos.
    palabras = entrada_usuario.lower().split()
    
    # Usamos un bucle 'for' para iterar sobre nuestro diccionario de reglas.
    for grupo_claves, respuestas in respuestas_por_palabra_clave.items():
        # Usamos otro bucle 'for' anidado para revisar cada palabra clave en el grupo.
        for clave in grupo_claves:
        
        # Detección de acciones claves
         if clave not in acciones_claves:
            # Si encontramos una palabra clave, seleccionamos una respuesta estandar.
            # Detección de palabras claves
            if clave in palabras:
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
        else:
            if clave == "adios" or "adiós":
                mensaje = "Adiós, espero que estes satisfecho."
                return mensaje
            elif clave == "catalogo" or "catálogo":
                Catalogo()
            elif clave == "caró" or "caro":
                mensaje = ""
            elif clave == "colocar":
                Hacer_Carrito()
                mensaje = ""
            elif clave == "carrito":
                Leer_Carrito()
                mensaje = ""
            elif clave == "comprar":
                mensaje = ""
            else:
                mensaje = "Lo siento, no entiendo la accion que tratas de hacer\nPorfavor vuelve a intentar"

            #Imprimir(mensaje)
        


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
        Imprimir(respuesta, voz)
        
        # INICIO DE LA EJECUCIÓN -
        # Para probar el chatbot en tu libreta, simplemente descomenta y ejecuta la siguiente línea.




# sys.argv[1] nombre del usuario
# sys.argv[2] voz 0 == activada
#             voz 1 == desactivada
# Yo se, puede llegar a ser algo confuso

eliza_chat(sys.argv[1], int(sys.argv[2]))