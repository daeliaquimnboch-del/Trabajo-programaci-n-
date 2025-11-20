def contar_lineas(nombre_archivo):
    with open(nombre_archivo, "r") as archivo:
        return len(archivo.readlines())
        