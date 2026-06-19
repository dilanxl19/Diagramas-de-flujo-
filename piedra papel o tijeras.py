#bienvenida al juego
print("hola bienvenido al juego de piedra papel o tijeras")
nombre = input("cual es tu nombre?: ")
print("hola", nombre)

# usuario interactua con la computadora

print("marca una opcion con el numero: ")
print("1. piedra")
print("2. papel")
print("3. tijeras")

#seleccion de opciones

opcion = int(input("elige tu opcion: "))
if  opcion == 1:
      print("elegiste piedra")
elif opcion == 2:
      print("elegiste papel")
elif opcion == 3:
      print("elegiste tijeras")
else:
      print("opcion no valida")

# la computadora eligira una opcion al azar
#sea piedra, papel o tijeras


