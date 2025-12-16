dolar_euro = 0.91
libra_euro = 1.18

opcion = input("¿Qué conversión deseas realizar?\n"
                "a) Dólares a Euros\n"
                "b) Euros a Dólares\n"
                "c) Libras a Euros\n"
                "d) Euros a Libras\n"
                "Escribe tu opción (a, b, c, d): ")

texto_usuario = "Introduce la cantidad de {} a convertir: "

if opcion == "a":
    cantidad_de_dinero = float(input(texto_usuario.format("dólares")))
    print("La cantidad en euros es: {}".format(cantidad_de_dinero * dolar_euro))

elif opcion == "b":
    cantidad_de_dinero = float(input(texto_usuario.format("euros")))
    print("La cantidad en dolares es: {}".format(cantidad_de_dinero / dolar_euro))

elif opcion == "c":
    cantidad_de_dinero = float(input(texto_usuario.format("libras")))
    print("La cantidad en euros es: {}".format(cantidad_de_dinero * dolar_euro))

elif opcion == "d":
    cantidad_de_dinero = float(input(texto_usuario.format("euros")))
    print("La cantidad en libras es: {}".format(cantidad_de_dinero / dolar_euro))

else:
    print("Opción no válida")
    exit()