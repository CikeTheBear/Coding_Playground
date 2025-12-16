titulo = "Bienvenidos al test del queso"
print("\n" + titulo + "\n" + "-" * len(titulo) + "\n")

puntuacion = 0

opcion = input("Pregunta 1: Que haces cuando ves una tabla de quesos?\n"
               "a) Salgo corriendo\n"
               "b) Pruebo uno de los quesos o incluso varios\n"
               "c) No puedo evitar devorarlos todos\n"
               "Escriba su opción (a, b, c): ")

if opcion == "a":
    puntuacion += 0

elif opcion == "b":
    puntuacion += 5

elif opcion == "c":
    puntuacion += 10

else:
    print("Opción no válida")
    exit()


opcion = input("\nPregunta 2: Como te gusta la hamburguesa?\n"
               "a) Sin queso\n"
               "b) Con queso\n"
               "c) Pan y queso\n"
               "Escriba su opción (a, b, c): ")

if opcion == "a":
    puntuacion += 0

elif opcion == "b":
    puntuacion += 5

elif opcion == "c":
    puntuacion += 10

else:
    print("Opción no válida")
    exit()


opcion = input("\nPregunta 3: Eres intolerante a la lactosa?\n"
               "a) Si\n"
               "b) A veces\n"
               "c) No\n"
               "Escriba su opción (a, b, c): ")

if opcion == "a":
    puntuacion += 0

elif opcion == "b":
    puntuacion += 5

elif opcion == "c":
    puntuacion += 10

else:
    print("Opción no válida")
    exit()



if (puntuacion <= 10):
    print("Eres más de chocolate que de queso")

elif (puntuacion <= 20):
    print("Eres un amante del queso")

else:
    print("Eres un queso roquefort con patas")