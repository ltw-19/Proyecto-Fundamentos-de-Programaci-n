#Proyecto
#Integrantes: 
# Luis Terrones C.I:  
# Sebastian Veloso  C.I: 32.153.454

def calculadro_de_puntajes(contraseña):
    
    puntos = 0
    minuscula = "abcdefghijklmnñopqrstuvwxyz"
    mayuscula = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    numeros = "0123456789"
    simbolos = "@$%&*~`/!#"

    tiene_minuscula = False
    tiene_mayuscula = False
    tiene_numero = False
    tiene_simbolo = False
    cantidad_simbolos = 0

    #Se analizan los caracteres
    for i in contraseña:
        if i in minuscula:
            tiene_minuscula = True 

        if i in mayuscula:
            tiene_mayuscula = True 
        if i in numeros:
            tiene_numero = True 
            cantidad_simbolos = cantidad_simbolos + 1
        if i in simbolos:
            tiene_simbolos = True

    for i in numeros: 
            tiene_numero = True 
            cantidad_simbolos = cantidad_simbolos + 1

