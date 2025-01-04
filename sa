# Proyecto
# Integrantes: 
# Luis Terrones C.I:  
# Sebastian Veloso  C.I: 32.153.454

# Constantes
MINUSCULAS = "abcdefghijklmnñopqrstuvwxyz"
MAYUSCULAS = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
NUMEROS = "0123456789"
SIMBOLOS = "@$%&*~`/!#"

# Simulación de lectura de archivos
CONTRASEÑAS = [
    "ejemplo1", "password123", "miContraseñaFuerte",  # Añade más contraseñas según sea necesario
]

PATRONES_PROHIBIDOS = [
    "CONTRASEÑA", "contraseña", "Contraseña",
    "123456", "QWERTY", "qwerty", "Qwerty",
    "MONO", "mono", "Mono", "INGRESO", "ingreso", "Ingreso",
    "BIENVENIDO", "bienvenido", "Bienvenido", "SOL", "sol", "Sol",
    "FUTBOL", "futbol", "Futbol", "BEISBOL", "beisbol", "Beisbol",
    "TEQUIERO", "tequiero", "Tequiero", "PRINCESA", "princesa", "Princesa",
    "ADMIN", "admin", "Admin", "DRAGON", "dragon", "Dragon", "MAESTRO",
    "maestro", "Maestro", "SOMBRA", "sombra", "Sombra", "SUPERMAN",
    "superman", "Superman", "BATMAN", "batman", "Batman", "CONFIANZA",
    "confianza", "Confianza", "1234567890", "ABC123", "abc123", "Abc123",
    "123123", "SECRETO", "secreto", "Secreto", "ACCESO", "acceso", "Acceso",
    "SEGURIDAD", "seguridad", "Seguridad", "PRIVADO", "privado", "Privado",
    "PROTECCION", "proteccion", "Proteccion", "CONFIDENCIAL", "confidencial",
    "Confidencial", "CONFIABLE", "confiable", "Confiable", "USUARIO", 
    "usuario", "Usuario", "CLAVE", "clave", "Clave", "PROTEGER", "proteger",
    "Proteger", "PROTEGIDO", "protegido", "Protegido", "HOLA", "hola", 
    "Hola", "CHAO", "chao", "Chao", "SALUDO", "saludo", "Saludo", "ADIOS", 
    "adios", "Adios", "NOMBRE", "nombre", "Nombre", "AGUA", "agua", "Agua",
    "LAPTOP", "laptop", "Laptop", "COMPUTADORA", "computadora", 
    "Computadora", "TELEFONO", "telefono", "Telefono", "098765", "CARRO",
    "carro", "Carro", "NOLOSE", "nolose", "Nolose", "HORSE", "horse", 
    "Horse", "BATTERY", "battery", "Battery", "BATERIA", "bateria", 
    "Bateria"
]

def calculador_de_puntajes(contraseña):
    while len(contraseña) < 8:
        print("La contraseña tiene que tener como mínimo 8 caracteres, introduzca de nuevo: ")
        contraseña = input("Introduzca su contraseña: ")  # Pedir al usuario que introduzca de nuevo la contraseña
    return contraseña

def calculadora_de_puntajes(contraseña): 
    puntos = 0
    minusculas = "abcdefghijklmnñopqrstuvwxyz"
    mayusculas = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    numeros = "0123456789"
    simbolos = "@$%&*~`/!#"

    tiene_minuscula = False
    tiene_mayuscula = False
    tiene_numero = False
    tiene_simbolo = False
    
    cantidad_minusculas = 0
    cantidad_mayusculas = 0
    cantidad_numeros = 0
    cantidad_simbolos = 0

    # Se analizan los caracteres
    for i in contraseña:
        puntos += 1  # 1 punto por cada carácter
        
        if i in minusculas:
            tiene_minuscula = True 
            cantidad_minusculas += 1
            puntos += 1

        elif i in mayusculas:
            tiene_mayuscula = True 
            cantidad_mayusculas += 1
            puntos += 1
            
        elif i en numeros:
            tiene_numero = True 
            cantidad_numeros += 1
            puntos += 1
            
        elif i en simbolos:
            tiene_simbolo = True
            cantidad_simbolos += 1
            puntos += 1

    if tiene_minuscula: 
        puntos += 1  # 1 punto si hay minúsculas

    if tiene_mayuscula: 
        puntos  += 1  # 1 punto si hay mayúsculas
        
    if tiene_numero: 
         puntos += 1  # 1 punto si hay números
        
    if tiene_simbolo: 
        puntos += 3  # 3 puntos si hay al menos un símbolo
        puntos += 2 * (cantidad_simbolos - 1)  # 2 puntos adicionales por cada símbolo extra

    return puntos

# Validar longitud y calcular puntaje para cada contraseña en el arreglo
for contraseña in CONTRASEÑAS:
    if any(patron in contraseña for patron in PATRONES_PROHIBIDOS):
        print(f"La contraseña '{contraseña}' contiene un patrón obvio y no es válida.")
    else:
        contraseña = calculador_de_puntajes(contraseña)
        resultado = calculadora_de_puntajes(contraseña)
        if resultado >= 15: 
            se_clasifica_en = "fuerte" 
        elif resultado >= 10: 
            se_clasifica_en = "moderada" 
        else: 
            se_clasifica_en = "débil"

        # Imprimir el resultado
        print(f"La contraseña '{contraseña}' tiene {resultado} puntos y se clasifica en {se_clasifica_en}.")
