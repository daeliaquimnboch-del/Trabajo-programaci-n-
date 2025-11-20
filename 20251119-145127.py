def contar_palabra(nombre_archivo, palabra):
    with open(nombre_archivo, "r") as archivo:
        texto = archivo.read().lower()
    return texto.count(palabra.lower())
    