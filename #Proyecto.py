#Proyecto
#Integrantes: 
# Luis Terrones C.I:  
# Sebastian Veloso  C.I: 32.153.454

def calculadro_de_puntajes(contraseña):
    if len(contrasena) < 8
    return "La contrasena tiene que tenerm inimo 8 caracteres"
    
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
            cantidad_minuscu += 1

        if i in mayuscula:
            tiene_mayuscula = True 
            cantidad_mayuscula += 1
            
        if i in numeros:
            tiene_numero = True 
            cantidad_numeros += 1
            
            cantidad_simbolos 
        if i in simbolos:
            tiene_simbolos = True
            cantidad_simbolos += 1

        puntos += len(contrasena) #1 punto por cada caracter 


