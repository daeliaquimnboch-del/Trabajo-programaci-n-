def ingresar_calificaciones():
    n = int(input("¿Cuántas calificaciones desea ingresar?: "))
    calificaciones = []

    for i in range(n):
        nota = float(input(f"Ingrese calificación #{i+1}: "))
        calificaciones.append(nota)

    print("Calificaciones ingresadas:", calificaciones)

    with open("calificaciones.txt", "w") as archivo:
        for nota in calificaciones:
            archivo.write(str(nota) + "\n")
            