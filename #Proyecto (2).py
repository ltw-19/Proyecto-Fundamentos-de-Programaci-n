#Proyecto
#Integrantes: 
# Luis Terrones C.I: 31.870.499
# Sebastian Veloso  C.I: 32.153.454

#Se lee el archivo de contraseñas
def leer_archivo(nombre_de_archivo):
    archivo = open(nombre_de_archivo, 'r', encoding="utf-8")
    contenido = archivo.read() #Se lee el contenido y se guarda en la variable contenido
    archivo.close() #Se cierra el archivo

    lineas = [] #Se inicializa lineas como un arreglo vacio que almacenara las lineas del archivo de texto
    linea_actual = "" #Aqui se inicializa una cadena vacia que se empleara para crear cada linea del archivo
    for caracter in contenido:
        if caracter == '\n': #Se verifica si el caracter actual es un salto de linea
            lineas.append(linea_actual) #Si lo es, se agrega la linea actual al arreglo lineas
            linea_actual = "" #Se reinicia a una cadena vacia para comenzar a crear cada linea
        else:
            linea_actual += caracter 
            #En este caso si no hay salto de linea se va agregando el caracter 
            #a la variable actual
    if linea_actual: 
        #Esto significa si la linea actual no esta vacia, es decir si existe una linea sin un salto de
        #linea al final, se agrega la "linea_actual" al arreglo "lineas"
        lineas.append(linea_actual)
    return lineas #Esto retorna todas las lineas del archivo de texto como un arreglo

#Aqui se calculan los puntajes
def calculadora_de_puntajes(contraseña, patrones_contraseña):
    patron = 0
    puntos = 0
    minuscula = "abcdefghijklmnñopqrstuvwxyz"
    mayuscula = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    numeros = "0123456789"

    tiene_minuscula = False
    tiene_mayuscula = False
    tiene_numero = False
    tiene_simbolo = False

    cantidad_simbolos = 0

    #Se analizan los caracteres
    for i in contraseña:
        puntos += 1
        if i in minuscula:
            tiene_minuscula = True 

        elif i in mayuscula:
            tiene_mayuscula = True 
            
        elif i in numeros:
            tiene_numero = True 
            
        else:   #Esta es una manera mas rapida de comprobar si tiene simbolo, ya que, con otro if y usando una
                #variable simbolo que contenga todos los simbolos seria mas complejo
            tiene_simbolo = True
            cantidad_simbolos += 1

    #Estos puntos se hacen separados, ya que, solo se suma un punto si existen letras minusculas, mayusculas, entre otros.
    #y no se toman en cuenta cuantas minusculas, mayusculas o numeros tienen
    if tiene_minuscula == True:
        puntos += 1
    
    if tiene_mayuscula == True:
        puntos +=1
    
    if tiene_numero == True:
        puntos += 1
    
    if tiene_simbolo == True:
        puntos += 3
        if cantidad_simbolos > 1:
            puntos += 2 * (cantidad_simbolos - 1) #Aqui se realiza un incremento de la variable.
            #En primer lugar se resta el valor de la cantidad de simbolos -1. Luego ese resultado se multiplica por 2.
            #Después ese valor resultante se suma al valor de puntos. Esto se hace para verificar y sumar si hay 
            #simbolos diferentes, si hay simbolos adicionales al primero se otroga dos puntos mas por cada simbolo
        
    for patron in patrones_contraseña:
        if patron in contraseña:
            puntos -= 5
    return puntos

#Esta funcion clasifica la contraseña segun el puntaje 
def clasificacion_de_contraseñas(puntos):
    if puntos >= 15:
        return "Fuerte"
    elif puntos >= 10:
        return "Moderada"
    else:
        return "Debil"

#Se ordena el arreglo de contraseñas de mayor a menor utilizando el ordenamiento por burbuja
def ordenar_contraseña(arreglo_contraseñas):
    for i in range (0, len(arreglo_contraseñas), 1):
        for j in range (0, len(arreglo_contraseñas)-1, 1):
            if arreglo_contraseñas[j][1] < arreglo_contraseñas[j+1][1]: 
                #Se compara el segundo elemento de indice 1
                #de la contraseña en la posicion "j" con el segundo elemento de la contraseña en la posicion "j+1".
                #Por lo tanto, si el segundo elemento de "arreglo_contraseñas[j]" es menor que el de
                #"arreglo_contraseñas[j+1]" se intercambiara estos dos elementos
                aux = arreglo_contraseñas[j]
                arreglo_contraseñas[j] = arreglo_contraseñas[j+1]
                arreglo_contraseñas[j+1] = aux

    return arreglo_contraseñas

#Se exporta el archivo usando un ciclo con multiples iteradores, esto hace que se itere el arreglo de contraseñas
#con cada uno de sus elementos
def exportar_archivo (nombre_archivo, contraseñas): #Aqui se define a la funcion con dos parametros, la primera que es el nombre del archivo
    #donde se exportará los datos y la segunda un arreglo donde contiene las contraseñas, sus puntos y sus categorias
    archivo = open(nombre_archivo, "w", encoding="utf-8") 
    #Se abre el archivo con el nombre en modo de escritura "w". En tal caso que el archivo no exista se creará.
    for contraseña, puntos, categoria in contraseñas: #Se itera el arreglo contraseñas con tres iteradores: contraseña, puntos y categoria
        archivo.write(contraseña + " | " + categoria + " | " + str(puntos) + "\n") 
        #En cada posicion se escribe una linea en el archivo, esa linea contiene la contraseña, la categoria y los puntos. El "\n" es para
        #asegurar que cada linea se escriba en una nueva linea

    archivo.close() #Se cierra el archivo

#Esta funcion realiza la ejecucion completa
def realizar_ejecucion ():
    #Se lee los dos archivos
    contraseñas = leer_archivo("Proyecto/Contraseñas - Proyecto (Fundamentos de Programación).txt")
    patrones = leer_archivo("Proyecto/Patrones obvios de contraseña - Proyecto (Fundamentos de Programación).txt")

    #El arreglo resultados se inicializa en vacio
    resultados = []
    #Se asignan los valores llamando a cada funcion correspondiente. Primero los puntos, luego a traves del parametro
    # de puntos se realiza la funcion de categoria
    for contraseña in contraseñas:
        puntos = calculadora_de_puntajes(contraseña, patrones)
        categoria = clasificacion_de_contraseñas(puntos)
        resultados.append([contraseña, puntos, categoria]) 
        #Esto agrega el arreglo de tres elementos a la variable resultados

    #Se ordena la contraseñas mediante las contraseñas en la variable resultados
    ordenar_contraseña(resultados)

    #Se exporta el archivo con los resultados
    exportar_archivo("resultado_contraseñas.txt", resultados)

    print("El proceso de creacion del archivo ha finalizado 'resultados_contraseñas.txt' generado")
    print("Gracias por utilizar nuestro clasificador de contraseñas")
    print("Hasta luego")

#Esta funcion da la bienvenida al usuario
def bienvenida():
    print("Bienvenido al clasificador de contraseñas")
    print("Este programa ejecutara un archivo de texto con contraseñas, los ordenara y clasificara segun su puntaje")
    print('Pulse "S" para continuar')
    print('Pulse "N" para salir')
    respuesta = input("introduzca una opcion: ")
    if respuesta == "S":
        realizar_ejecucion()
    elif respuesta == "N":
        return 0
    else: #Si el usuario introdujo una opcion invalida se crea un bucle hasta que el usuario digite una opcion válida
        while True:
            print("Favor introduzca una opcion válida")
            print('Pulse "S" para continuar')
            print('Pulse "N" para salir')
            respuesta = input("Introduzca una opcion: ")
            if respuesta == "S":
                realizar_ejecucion()
                break
            elif respuesta == "N":
                return 0

#Aqui se llama a la funcion de bienvenida
bienvenida ()
