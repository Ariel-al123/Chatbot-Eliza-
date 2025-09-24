import random
import streamlit as st
import time
import sys
import pyttsx3
import os

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
        Imprimir(respuesta, voz)
        
        # INICIO DE LA EJECUCIÓN -
        # Para probar el chatbot en tu libreta, simplemente descomenta y ejecuta la siguiente línea.




# sys.argv[1] nombre del usuario
# sys.argv[2] voz 0 == activada
#             voz 1 == desactivada
# Yo se, puede llegar a ser algo confuso
print(sys.argv[2])
eliza_chat(sys.argv[1], int(sys.argv[2]))
    