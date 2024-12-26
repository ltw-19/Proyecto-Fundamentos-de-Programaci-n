#Proyecto
#Integrantes: 
# Luis Terrones C.I:  
# Sebastian Veloso  C.I: 32.153.454

contraseña = input("Introduzca su contraseña: ")

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
            
        elif i in numeros:
            tiene_numero = True 
            cantidad_numeros += 1
            puntos += 1
            
        elif i in simbolos:
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

# Validar longitud y calcular puntaje
contraseña = calculador_de_puntajes(contraseña)
resultado = calculadora_de_puntajes(contraseña)

# Clasificación de la contraseña 
if resultado >= 15: 
    se_clasifica_en = "fuerte" 
elif resultado >= 10: 
    se_clasifica_en = "moderada" 
else: 
    se_clasifica_en = "débil"

# Imprimir el resultado
print("Tu contraseña tiene", resultado, "puntos y se clasifica en", se_clasifica_en)
