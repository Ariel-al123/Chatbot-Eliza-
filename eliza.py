import random
import time
import sys
import pyttsx3
import os


# crea funciones donde se guarden las carcteristicas tecnicas en un archivo
# otro en donde se guarde la recomendacion anterior 

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
        time.sleep(0.001)
    print()  # Salto de línea al final
    
   
    engine.runAndWait()


def Hacer_Carrito(objetos):
    
    ProductoEncontrado = False
    PrecioEncontrado = False
    DescuentoEncontrado = False
    lineas = []  # Almacenar todas las líneas del archivo

    # Leer todas las líneas del archivo
    with open("catalogo.txt", "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()

    # Recorrer las líneas con un índice para controlar los saltos
    for i in range(len(lineas)):
        # Convertir la línea actual a minúsculas y dividirla en palabras
        linea_actual = lineas[i].strip().lower().split()

        # Buscar el objeto en la línea actual
        if objetos in linea_actual:
            
            Producto = lineas[i].strip()
            ProductoEncontrado = True
            # Buscar el precio en la siguiente línea (1 salto)
            if i + 1 < len(lineas):
                siguiente_linea = lineas[i + 1].strip()
                if "$" in siguiente_linea:
                    
                    Precio = siguiente_linea.split("$", 1)[1].strip()
                    PrecioEncontrado = True
                    # Buscar el descuento 6 líneas después
                    if i + 7 < len(lineas):  # 1 para precio + 6 para descuento
                        linea_descuento = lineas[i + 7].strip()
                        if "%" in linea_descuento:
                            # Extraer el número antes del %
                            Descuento = linea_descuento.split("%")[0].strip().split()[-1]
                            DescuentoEncontrado = True
                            break  # Salir del bucle tras encontrar todo
                        else:
                            print("No se encontró el descuento en la línea esperada.")
                    else:
                        print("No hay suficientes líneas para encontrar el descuento.")
                else:
                    print("No se encontró el precio en la línea esperada.")
            else:
                print("No hay suficientes líneas para encontrar el precio.")
    
   
    if not ProductoEncontrado:
        print(f"El objeto '{objetos}' no se encontró en el catálogo.")
    elif not PrecioEncontrado:
        print("No se encontró el precio del objeto.")
    elif not DescuentoEncontrado:
        print("No se encontró el descuento del objeto.")
    
    # Retornar los datos encontrados (si los hay)
    if ProductoEncontrado and PrecioEncontrado and DescuentoEncontrado:
        return f"Nombre : {Producto},\nPrecio : {Precio},\nDescuento : {Descuento}%\nProducto en el carrito listo ✔️"
        
   

    #Guardar informacion en carrito.txt
    with open("carrito.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"Producto: {Producto}\n")
        archivo.write(f"Precio: ${Precio}\n")
        archivo.write(f"Descuento: {Descuento}%\n\n")
    
    
    

def Leer_Carrito():
    with open("carrito.txt", "r", encoding="utf-8") as archivo:
        contenido = archivo.read()
    return contenido


def Catalogo():
    with open("catalogo.txt", "r", encoding="utf-8") as archivo:
        contenido = archivo.read()
    return contenido

def Eliminar_Carrito():
    # Mostrar carrito y escribir el nombre del producto a eliminar
    # Cada 1 lineas es un producto
        # Nombre
        # Precio
        # Descuento
        # Espacio

    return

def Comprar(saldo):
    # Obtener saldo/dinero al principio en el main
    # Mostrar carrito
    # Obtener precios, descuentos
    # Mostrar descuento cada uno y el subtotal
    # Mostrar la cantidad total a pagar
     # Si es negativo el la cantidad preguntar si desea eliminar productos del carrito
     # y retornar a Eliminar_Carrito()
        # Preguntar de esta forma (S/n)
     # sino sales de la funcion
    # Preguntar si desea confirmar la compra (S/n)
    # Restar el total del carrito al saldo/dinero
    # Mostrar el saldo/dinero restante

    return



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


catalogo_productos_todo = {
    "laptops": [
        {
            "nombre": "laptop1",
            "precio": 15000.00,
            "caracteristicas": [
                "16GB RAM", "RTX 3060", "SSD 512GB",
                "Intel i7 11ª Gen"
            ],
            "palabras_clave": (
                "3060", "rtx", "intel", "ssd", "16", "ram", "i7"
            ),
            "descuento_maximo": 0.15
        },
        {
            "nombre": "laptop2",
            "precio": 12000.00,
            "caracteristicas": [
                "8GB RAM", "Intel i5 12ª Gen", "SSD 256GB"
            ],
            "palabras_clave": (
               "8gb", "intel", "i5", "256", "ssd"
            ),
            "descuento_maximo": 0.10
        },
        {
            "nombre": "laptop3",
            "precio": 25000.00,
            "caracteristicas": [
                "32GB RAM", "RTX 4070", "SSD 1TB",
                "Intel i9 13ª Gen"
            ],
            "palabras_clave": (
                "nvidia", "4070", "intel", "i9", "ssd", "1tb", "ram", "32"
            ),
            "descuento_maximo": 0.20
        }
    ],

    "pc": [
        {
            "nombre": "pc1",
            "precio": 8000.00,
            "caracteristicas": [
                "8GB RAM", "Ryzen 5 5600G",
                "SSD 480GB"
            ],
            "palabras_clave": (
               "ryzen", "amd", "480", "ssd", "5600", "ram", "8"
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
                "nvidia", "ryzen", "3060", "16", "ram", "ti", "ssd", "1tb", "rtx"
            ),
            "descuento_maximo": 0.18
        },
        {
            "nombre": "pc3",
            "precio": 35000.00,
            "caracteristicas": [
                "64GB RAM", "RTX 4090",
                "SSD 2TB NVMe", "Intel i9 14 gen"
            ],
            "palabras_clave": (
               "intel", "4090", "nvidia", "ssd", "2tb", "ram", "64", "rtx", "pc"
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



def generar_respuesta(entrada_usuario, saldo):

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
        "catalogo", "catálogo",
        "caró", "caro",
        "colocar", "carrito",
        "comprar"
    }

    palabras_clave_recomendacion = {
        "requisitos", "recomendación", "recomendacion", "recomiendame",
        "sugerencia", "sugerencias",
        "buscar", "busca", "busco", "encontrar", "encuentra", "encuentro",
        "necesito", "necesito", "quiero", "quiero",
        "deseo", "ayuda", "ayudar", "ayúdame", "ayudame",
    }

    palabras_clave_requisitos = {
        "nvidia", "rtx", "intel", "i5", "i7", "i9",
        "ryzen", "amd", "ssd", "tb", "gb", "ram",
        "ti", "gen"
    }

    sinonimos_de_PC = {
        "pc", "computadora", "ordenador", "escritorio"
    }

    sinonimos_de_laptop = {
        "laptop", "portátil", "portatil" ,"notebook"
    }

    # Convertimos la entrada a una lista de palabras en minúsculas y las separamos.
    palabras = entrada_usuario.lower().split()
    retorno_valor = False
    # 🔹 Acciones Claves
    for i in range(len(palabras)):
        palabra = palabras[i]
        if palabra in acciones_claves:
            if palabra in ("adios", "adiós"):
                sys.exit()
                return "Adiós, espero que estés satisfecho."
            elif palabra in ("catalogo", "catálogo"):
                retorno_valor = True
                mensaje = Catalogo()
                return mensaje
            elif palabra in ("caró", "caro"):
                retorno_valor = True
                return "La opción 'caro' no está implementada. Por favor, intenta otra acción."
            elif palabra == "colocar":
                retorno_valor = True
                producto = palabras[i + 1]  # la siguiente palabra
                print(f"Producto a buscar: {producto}")
                if producto.startswith("pc") or producto.startswith("laptop"):
                        a = Hacer_Carrito(producto)
                        return a
                else:
                    retorno_valor = True
                    return "Producto no encontrado en el catálogo ❌"
            elif palabra == "carrito":
                retorno_valor = True
                a = Leer_Carrito()
                return a
            elif palabra == "comprar":
                retorno_valor = True
                Comprar(saldo)
                return "Simulación de compra realizada."
            


    # 🔹 Buscamos en recomendaciones
    for i in range(len(palabras)):
        palabra = palabras[i]
        if palabra in palabras_clave_recomendacion:
            # Buscar requisitos en la misma entrada
            requisitos = [p for p in palabras if p in palabras_clave_requisitos]
            if requisitos:
                # Determinar si el usuario busca una laptop o PC
                tipo_dispositivo = None
                # Any verifica si al menos un elemento cumple la condición
                if any(p in palabras for p in sinonimos_de_laptop):
                    tipo_dispositivo = "laptops"
                elif any(p in palabras for p in sinonimos_de_PC):
                    tipo_dispositivo = "pc"
                
                if tipo_dispositivo:
                    # Filtrar productos que coincidan con los requisitos
                    productos_recomendados = []
                    for producto in catalogo_productos_todo[tipo_dispositivo]:
                        # Solo recomienda si cumple al menos 2 requisitos
                        coincidencias = sum(1 for req in requisitos if req in producto["palabras_clave"])
                        if coincidencias >= 1:
                            productos_recomendados.append(producto)
                    # Ordenar de mayor a menor precio
                    productos_recomendados.sort(key=lambda x: x["precio"], reverse=True)
                    
                    if productos_recomendados:
                        retorno_valor = True
                        respuesta = "Basado en tus requisitos, te recomiendo:\n"
                        for prod in productos_recomendados:
                            respuesta += f"- {prod['nombre']} (${prod['precio']}) con características: {', '.join(prod['caracteristicas'])}\n"
                        return respuesta
                    else:
                        retorno_valor = True
                        respuesta = "No encontré productos que coincidan exactamente con tus requisitos."
                        return respuesta
                else:
                    retorno_valor = True
                    respuesta = "Por favor, especifica si buscas una laptop o una PC."
                    return respuesta
            else:
                retorno_valor = True
                respuesta = "No encontré productos que coincidan exactamente con tus requisitos."
                return respuesta
    

    # 🔹 Si no es acción clave → buscamos en respuestas normales
    if not retorno_valor or respuesta == None:
        for grupo_claves, respuestas in respuestas_por_palabra_clave.items():
            for clave in grupo_claves:
                if clave in palabras:
                    if clave in palabras_clave and len(palabras) > 2:
                        frase_reflejada = []
                        for palabras in palabras:  # Error: la variable 'palabras' está siendo sobrescrita
                          frase_reflejada.append(cambio_pronombres.get(palabras, palabras))
                        return "¿Dices que " + " ".join(frase_reflejada) + "?"
                    else:
                        return random.choice(respuestas)


def eliza_chat(name_user, voz, saldo):
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
        
            #Si no salimos, llamamos a nuestra función principal para obtener una respuesta.
    
        respuesta = generar_respuesta(entrada_usuario, saldo)
        #f-string (cadena formateada) es una forma moderna y legible de insertar variables en texto.
        Imprimir(respuesta, voz)
        
        # INICIO DE LA EJECUCIÓN -
        # Para probar el chatbot en tu libreta, simplemente descomenta y ejecuta la siguiente línea.




# sys.argv[1] nombre del usuario
# sys.argv[2] voz 0 == activada
#             voz 1 == desactivada
# Yo se, puede llegar a ser algo confuso

eliza_chat(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))