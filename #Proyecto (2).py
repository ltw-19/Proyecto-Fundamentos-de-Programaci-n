#Proyecto
#Integrantes: 
# Luis Terrones C.I: 31.870.499
# Sebastian Veloso  C.I: 32.153.454

arreglo = []
def leer_archivo (archivo):
    arreglo = []
    return arreglo

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

        if i in mayuscula:
            tiene_mayuscula = True 
            
        if i in numeros:
            tiene_numero = True 
            
        if i in simbolos:
            tiene_simbolo = True
            cantidad_simbolos += 1

    
    if tiene_minuscula:
        puntos += 1
    
    if tiene_mayuscula:
        puntos +=1
    
    if tiene_numero:
        puntos += 1
    
    if tiene_simbolo == True:
        puntos += 3
        if cantidad_simbolos > 1:
            puntos += 2 * (cantidad_simbolos - 1) #Aqui se realiza un incremento de la variable.
            #En primer lugar se resta el valor de la cantidad de simbolos -1. Luego ese resultado se multiplica por 2.
            #Luego ese valor resultante se suma al valor de puntos.

    return puntos

#Esta funcion clasifica la contraseña segun el puntaje 
def clasificacion_de_contraseñas(puntos):
    if puntos >= 15:
        return "Fuerte"
    elif puntos >= 10:
        return "Moderada"
    elif puntos < 10:
        return "Debil"

#Se ordena el arreglo de contraseñas de mayor a menor utilizando el ordenamiento por burbuja
def ordenar_contraseña(lista_de_contraseñas):
    for i in range (0, len(arreglo), 1):

        for j in range (0, len(arreglo)-1, 1):
            if arreglo[j] < arreglo[j+1]:
                aux = arreglo[j]
                arreglo[j] = arreglo[j+1]
                arreglo[j+1] = aux


resultado_puntajes = calculadora_de_puntajes(contraseña)
categoria = clasificacion_de_contraseñas(resultado_puntajes)
print(contraseña, "|", resultado_puntajes, "puntajes", "|",  categoria)
