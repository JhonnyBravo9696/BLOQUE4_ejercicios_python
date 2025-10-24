import os
agenda = {}

while True:
    os.system("clear")
    print("1. Añadir y modificar")
    print("2. Buscar")
    print("3. Borrar")
    print("4. Listar")
    print("5. Salir")
    opcion = input("Elige una opcion: ")


    if opcion == "1":
        nombre = input("introduce un nombre: ")
        if nombre in agenda:
            print(f"El numero actual es: {agenda}")
            modnum = input("¿Quieres modificarlo?(s/n): ")
            if modnum == "s":
                telefono = input("Introduce el nuevo telefono: ")
                agenda[nombre] = telefono


        else:
            telefono = input("Introduce el telefono: ")
            agenda[nombre] = telefono
            print("Contacto añadido con exito")


    if opcion == "2":
        buscar = input("Introduce un nombre para buscar: ")
        for nombre in agenda:
            if nombre.startswith(buscar):
                print(f"{nombre}: {agenda[nombre]}")



    if opcion == "3":
        nombre = input("Introduce el nombre a borrar: ")
        if nombre in agenda:
            borrar = input(f"¿Seguro que quieres borrar a {nombre}? (s/n): ")
            if borrar == "s":
                del agenda[nombre]
                print("Contacto borrado")



    if opcion == "4":
        for nombre, telefono in agenda.items():
            print(f"{nombre}: {telefono}")


    if opcion == "5":
        print ("guardando y saliendo...")
        break

    input ("pulsa lo que sea para continuar:")
