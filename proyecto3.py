import string

def validar_y_calcular_puntaje(contraseña: str) -> int:
    while len(contraseña) < 8:
        print("La contraseña debe tener al menos 8 caracteres. Por favor, ingrésala de nuevo:")
        contraseña = input("Introduce tu contraseña: ")

    puntos = 0
    tiene_minuscula = any(char.islower() for char in contraseña)
    tiene_mayuscula = any(char.isupper() for char in contraseña)
    tiene_digito = any(char.isdigit() for char in contraseña)
    tiene_simbolo = any(char in string.punctuation for char in contraseña)

    puntos += len(contraseña)
    if tiene_minuscula:
        puntos += 2
    if tiene_mayuscula:
        puntos += 2
    if tiene_digito:
        puntos += 2
    if tiene_simbolo:
        puntos += 3

    puntos += 2 * sum(char in string.punctuation for char in contraseña) - 1

    return puntos

contraseña = input("Introduce tu contraseña: ")
puntaje = validar_y_calcular_puntaje(contraseña)

if puntaje >= 15:
    fuerza = "fuerte"
elif puntaje >= 10:
    fuerza = "moderada"
else:
    fuerza = "débil"

print(f"Tu contraseña tiene {puntaje} puntos y se clasifica como {fuerza}.")

