#Proyecto
#Integrantes: 
# Luis Terrones C.I: 31.870.499
# Sebastian Veloso  C.I: 32.153.454

# arreglo_contraseñas = []
#Se lee el archivo de contraseñas
def leer_archivo():
    """Lee un archivo y retorna una lista de líneas"""
    archivo = open("Proyecto/Contraseñas - Proyecto (Fundamentos de Programación).txt", "r", encoding="utf-8")
    arreglo_contraseñas = archivo.readlines()
    return arreglo_contraseñas

#Se lee el archivo de patrones
def leer_archivo_patrones():
    archivo2 = open("Proyecto/Patrones obvios de contraseña - Proyecto (Fundamentos de Programación).txt", "r", encoding="utf-8")
    arreglo_patrones = archivo2.readlines()
    return arreglo_patrones

# contraseña = input("Introduzca su contraseña: ")
# puntos = 0

#Aqui se calculan los puntajes
def calculadora_de_puntajes(contraseña):
    # while len(contraseña) < 8:
    #     contraseña = input("La contraseña tiene que tener como minimo 8 caracteres, introduzca de nuevo: ")
    patron = 0
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

#Estos puntos se hacen separados, ya que, solo se suma un punto si existen letras minusculas, mayusculas, entre otros.
#y no se toman en cuenta cuantas minusculas o mayusculas tienen
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
            #Después ese valor resultante se suma al valor de puntos.
    # arreglo_patrones = leer_archivo_patrones()
    arreglo_patrones = leer_archivo_patrones()
    for patron in arreglo_patrones:
        if patron.strip() in contraseña:
            puntos -= 5
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
def ordenar_contraseña(arreglo_contraseñas):
    for i in range (0, len(arreglo_contraseñas), 1):

        for j in range (0, len(arreglo_contraseñas)-1, 1):
            if arreglo_contraseñas[j] < arreglo_contraseñas[j+1]:
                aux = arreglo_contraseñas[j]
                arreglo_contraseñas[j] = arreglo_contraseñas[j+1]
                arreglo_contraseñas[j+1] = aux
    return arreglo_contraseñas

#Se exporta el archivo usando un ciclo con multiples iteradores, esto hace que se itere el arreglo de contraseñas
#con cada uno de sus elementos
def exportar_archivo (nombre_archivo, contraseñas):
    archivo = open(nombre_archivo, "w", encoding="utf-8")
    for contraseña, puntos, categoria in contraseñas:
        archivo.write(contraseña + " | " + categoria + " | " + str(puntos) + "\n")

# resultado_puntajes = calculadora_de_puntajes(contraseña)
# categoria = clasificacion_de_contraseñas(resultado_puntajes)
# print(contraseña, "|", resultado_puntajes, "puntajes", "|",  categoria)

#Esta funcion realiza la ejecucion completa
def realizar_ejecucion ():
    #Se lee los dos archivos
    contraseñas = leer_archivo()
    patrones = leer_archivo_patrones()

    #El arreglo resultados se inicializa en vacio
    resultados = []
    #Se asignan los valores llamando a cada funcion correspondiente. Primero los puntos, luego a traves del parametro
    # de puntos se realiza la funcion de categoria
    for contraseña in contraseñas:
        puntos = calculadora_de_puntajes(contraseña)
        categoria = clasificacion_de_contraseñas(puntos)
        resultados.append([contraseña, puntos, categoria]) 
        #Esto agrega el arreglo de tres elementos a la variable resultados

    #Se ordena la contraseñas mediante las contraseñas en la variable resultados
    ordenar_contraseña(resultados)

    #Se exporta el archivo con los resultados
    exportar_archivo("resultado_contraseñas.txt", resultados)

    print("El proceso de creacion del archivo ha finalizado 'resultados_contraseñas.txt' generado")

while True:
    print("Bienvenido al clasificador de contraseñas")
    print('Pulse "S" para continuar')
    print('Pulse "N" para salir')
    respuesta = input("introduzca una opcion: ")
    if respuesta == "S":
        realizar_ejecucion()
        break
    elif respuesta == "N":
        break
    else:
        print("Favor introduzca una opcion válida")
        print('Pulse "S" para continuar')
        print('Pulse "N" para salir')
        respuesta = input("introduzca una opcion: ")
