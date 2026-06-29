import random
print("BIENVENIDO AL JUEGO PIEDRA, PAPEL O TIJERA")
# Pedir nombre al usuario
nombre = input("Escribe tu nombre: ")
print("Hola", nombre)
# Preguntar si quiere jugar de nuevo
jugar_de_nuevo = "si"
while jugar_de_nuevo == "si":
    print("Elige una opción:")
    print("1. piedra")
    print("2. papel")
    print("3. tijera")
    opcion = input("Escribe 1, 2 o 3: ")
# Validar opción
    if opcion == "1" or opcion == "2" or opcion == "3":
# Convertir número a palabra
        if opcion == "1":
            usuario = "piedra"
        elif opcion == "2":
            usuario = "papel"
        else:
            usuario = "tijera"  
        print("Tú elegiste:", usuario)
# Elección de la computadora (usando números del 1 al 3)
        numero_computadora = random.randint(1, 3)
        if numero_computadora == 1:
            computadora = "piedra"
        elif numero_computadora == 2:
            computadora = "papel"
        else:
            computadora = "tijera"
        print("La computadora eligió:", computadora)
# Determinar el resultado del juego
        if usuario == computadora:
            print("EMPATE")
# Casos donde el usuario gana escritos uno por uno (sin la barra '\')
        elif usuario == "piedra" and computadora == "tijera":
            print("GANASTE")
        elif usuario == "papel" and computadora == "piedra":
            print("GANASTE")
        elif usuario == "tijera" and computadora == "papel":
            print("GANASTE")
# Si no fue empate ni ganó, entonces perdió
        else:
            print("PERDISTE")
# Preguntar si quiere jugar otra vez (sin .lower(), esperando que escriba "si" en minúsculas)
        print("¿Deseas jugar de nuevo? (si/no):")
        jugar_de_nuevo = input()
    else:
        print("Opción no válida")
# Quitamos el 'continue' y dejamos que el ciclo repita de forma natural por el flujo del IF
print("Gracias por jugar")