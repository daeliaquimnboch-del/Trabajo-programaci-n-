
def guardar_estudiante(est):
    with open("estudiante.txt", "w") as archivo:
        for clave, valor in est.items():
            archivo.write(f"{clave}: {valor}\n")
            