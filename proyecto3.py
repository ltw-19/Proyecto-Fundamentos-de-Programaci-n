import string

def validar_y_calcular_puntaje(contrasena:str) -> int:
    while len(contrasena) < 8:
        print("La contrasena tiene que tener mas de 8 caracteres")
        contrasena = input("introduzca su contrasena")

    puntos = 0
    tiene_minuscula = any(char.islower() for char in contrasena)
    tiene_mayuscula = any(char.isupper() for char in contrasena)
    tiene_numero = any(char.isdigit() for char in contrasena)
    tiene_simbolo = any(char in string.punctuation for char in contrasena)

    puntos += len(contrasena)
    if tiene_minuscula:
        puntos += 2
    if tiene_mayuscula:
        puntos += 2
    if tiene_numero:
        puntos += 2
    if tiene_simbolo:
        puntos += 3
        puntos += 2 * sum(char in string.punctuation for char in contrasena) - 1
