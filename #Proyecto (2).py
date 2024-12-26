#Proyecto
#Integrantes: 
# Luis Terrones C.I:  
# Sebastian Veloso  C.I: 32.153.454

contraseña = input("Introduzca su contraseña: ")
puntos = 0
def calculadora_de_puntajes(contraseña):
    while len(contraseña) < 8:
        contraseña = input("La contraseña tiene que tener como minimo 8 caracteres, introduzca de nuevo: ")

    puntos = 0
    minuscula = "abcdefghijklmnñopqrstuvwxyz"
    mayuscula = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    numeros = "0123456789"
    simbolos = "@$%&*~`/!#"

    tiene_minuscula = False
    tiene_mayuscula = False
    tiene_numero = False
    tiene_simbolo = False
    
    cantidad_minuscu = 0
    cantidad_mayusculas = 0
    cantidad_numeros = 0
    cantidad_simbolos = 0

    #Se analizan los caracteres
    for i in contraseña:
        puntos += 1
        if i in minuscula:
            tiene_minuscula = True 
            puntos += 1

        if i in mayuscula:
            tiene_mayuscula = True 
            puntos += 1
            
        if i in numeros:
            tiene_numero = True 
            puntos += 1
            
        if i in simbolos:
            tiene_simbolo = True
            puntos += 3
            cantidad_simbolos += 1
            if cantidad_simbolos > 1:
                puntos = 2 * (cantidad_simbolos - 1) #Aqui se realiza un incremento de la variable.
                #En primer lugar se resta el valor de la cantidad de simbolos -1. Luego ese resultado se multiplica por 2.
                #Luego ese valor resultante se suma al valor de puntos

    return puntos

#Esta funcion clasifica la contraseña segun el puntaje 
def clasificacion_de_contraseñas(puntos):
    if puntos >= 15:
        return "Fuerte"
    elif puntos >= 10:
        return "Moderada"
    elif puntos < 10:
        return "Debil"
    


resultado_puntajes = calculadora_de_puntajes(contraseña)
categoria = clasificacion_de_contraseñas(resultado_puntajes)
print(contraseña, "|", resultado_puntajes, "puntajes", "|",  categoria)
