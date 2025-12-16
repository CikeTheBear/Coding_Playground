opcion = input("¿Prefieres (A) iOS o (B) Android?: ")

if opcion == "A":
    opcion = input("Tienes dinero? (S/N): ")

    if opcion == "S":
        print("Compra un iPhone Pro Ultra Max")

    elif opcion == "N":
        print("Compra un iPhone de segunda mano")

    else:
        print("Opción no válida")
        exit()

elif opcion == "B":
    opcion = input("Tienes dinero? (S/N): ")

    if opcion == "S":
        opcion = input("Te importan las buenas fotos? (S/N): ")

        if opcion == "S":
            print("Compra un Google Pixel")

        elif opcion == "N":
            print("Compra un calidad/precio como un OnePlus")

        else:
            print("Opción no válida")
            exit()

    elif opcion == "N":
        print("Compra un Android chino de 100 euros")

    else:
        print("Opción no válida")
        exit()

else:
    print("Opción no válida")
    exit()