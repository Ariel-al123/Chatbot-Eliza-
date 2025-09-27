catalogo_productos_pc = {
    "laptop": {
        "precio": 15000.00,
        "caracteristicas": ["16GB RAM", "RTX 3060", "SSD 512GB", "Intel i7 11ª Gen", "144Hz"],
        "palabras_clave": ("laptop", "gaming", "juegos", "notebook", "pc", "portátil", "ordenador", "3060", "RTX", "intel", "gamer"),
        "descuento_maximo": 0.15
    },

    "laptop": {
        "precio": 12000.00,
        "caracteristicas": ["8GB RAM", "Intel i5 12ª Gen", "SSD 256GB", "Pantalla 14'' FHD", "Ligera"],
        "palabras_clave": ("laptop", "ultrabook", "ligera", "notebook", "trabajo", "portátil", "oficina"),
        "descuento_maximo": 0.10
    },

    "laptop": {
        "precio": 25000.00,
        "caracteristicas": ["32GB RAM", "RTX 4070", "SSD 1TB", "Intel i9 13ª Gen", "Pantalla 16'' QHD 240Hz"],
        "palabras_clave": ("laptop", "gaming", "profesional", "nvidia", "4070", "intel", "creadores", "render", "edición"),
        "descuento_maximo": 0.20
    },

    "pc escritorio": {
        "precio": 8000.00,
        "caracteristicas": ["8GB RAM", "Ryzen 5 5600G", "SSD 480GB", "Gráficos integrados Vega"],
        "palabras_clave": ("pc", "escritorio", "ordenador", "oficina", "básico", "amd", "trabajo"),
        "descuento_maximo": 0.08
    },

   "pc escritorio":  {
        "precio": 20000.00,
        "caracteristicas": ["16GB RAM", "RTX 3060 Ti", "SSD 1TB", "Ryzen 7 5800X"],
        "palabras_clave": ("pc", "gaming", "nvidia", "ryzen", "juegos", "gamer", "desempeño"),
        "descuento_maximo": 0.18
    },

    "pc escritorio":  {
        "precio": 35000.00,
        "caracteristicas": ["64GB RAM", "RTX 4090", "SSD 2TB NVMe", "Intel Xeon", "Placa base workstation"],
        "palabras_clave": ("pc", "workstation", "profesional", "render", "edición", "servidor", "intel", "4090", "nvidia"),
        "descuento_maximo": 0.25
    }
}


catalogo_productos_celulares = {
    "celular": {
        "precio": 3500.00,
        "caracteristicas": ["3GB RAM", "32GB Almacenamiento", "Cámara 13MP", "Pantalla 6.1'' HD+", "Batería 4000mAh"],
        "palabras_clave": ("celular", "smartphone", "android", "básico", "económico", "barato"),
        "descuento_maximo": 0.05
    },

    "celular": {
        "precio": 7500.00,
        "caracteristicas": ["6GB RAM", "128GB Almacenamiento", "Snapdragon 680", "Pantalla AMOLED 6.4'' FHD+", "Cámara 64MP", "Batería 5000mAh"],
        "palabras_clave": ("celular", "smartphone", "android", "gama media", "xiaomi", "samsung", "buena cámara", "batería"),
        "descuento_maximo": 0.10
    },

    "celular": {
        "precio": 12500.00,
        "caracteristicas": ["8GB RAM", "256GB Almacenamiento", "Snapdragon 870", "Pantalla AMOLED 120Hz", "Cámara 108MP", "Carga rápida 67W"],
        "palabras_clave": ("celular", "gaming", "android", "xiaomi", "realme", "fluido", "pantalla 120hz", "media-alta"),
        "descuento_maximo": 0.15
    },

    "celular": {
        "precio": 22000.00,
        "caracteristicas": ["12GB RAM", "512GB Almacenamiento", "Snapdragon 8 Gen 2", "Pantalla AMOLED QHD+ 120Hz", "Cámara 200MP", "Carga rápida 120W"],
        "palabras_clave": ("celular", "smartphone", "gaming", "android", "alta gama", "samsung", "xiaomi", "oneplus", "cámara pro"),
        "descuento_maximo": 0.20
    },

    "celular": {
        "precio": 28000.00,
        "caracteristicas": ["6GB RAM", "128GB Almacenamiento", "Chip A15 Bionic", "Pantalla OLED 6.1''", "Cámara dual 12MP", "iOS 16"],
        "palabras_clave": ("celular", "iphone", "apple", "ios", "premium", "iphone 13", "seguridad"),
        "descuento_maximo": 0.12
    },

    "celular": {
        "precio": 35000.00,
        "caracteristicas": ["8GB RAM", "256GB Almacenamiento", "Chip A17 Pro", "Pantalla OLED ProMotion 120Hz", "Cámara triple 48MP", "iOS 17"],
        "palabras_clave": ("celular", "iphone", "apple", "ios", "premium", "iphone 15 pro", "alta gama", "fotografía"),
        "descuento_maximo": 0.18
    }
}




respuestas_por_palabra_clave = {
    ("hola", "buenas", "hey", "qué tal"): [
        "Hola. Soy Eliza. Por favor, ¿En que puedo ayudate?.",
        "Hola, ¿En que puedo ayudate?",
        "Un gusto saludarte, hablame sobre de ti."
    ],

    ("adiós", "hasta luego", "chao", "nos vemos"): [
        "Adiós. Gracias por hablar conmigo.",
        "Hasta luego, esperto que estes satisfecho.",
        "Fue un placer conversar contigo. Adiós.",
        "Gracias vuelve pronto."
    ],
}