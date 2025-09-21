numero_secreto = 26

numero_jugador = int(input("Introduce el numero secreto: "))

if numero_secreto == numero_jugador:
    print("Felicidades, adivinaste!")
else:
    print("El numero introducido no es correcto")