temperatura_grados = float(input("Ingrese los grados de la temperatura: "))

sistema_temperatura = input("Ingrese el sistema de temperatura (C/F): ").lower()

if sistema_temperatura == "c":
    temperatura_grados = str((temperatura_grados * 9/5) + 32)
    print("La temperatura en grados Fahrenheit es: " + temperatura_grados + " F")
elif sistema_temperatura == "f":
    temperatura_grados = str((temperatura_grados - 32) * 5/9)
    print("La temperatura en grados Celsius es: " + temperatura_grados + " C")
else:
    print("El sistema de temperatura no es valido, por favor ingrese C o F")