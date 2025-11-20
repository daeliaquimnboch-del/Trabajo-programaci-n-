def saludar():
    mensaje = "Hola, bienvenido al curso de Programación I"
    
    # 1. Mostrar el mensaje en pantalla
    print(mensaje)
    
    # 2. Guardar el mensaje en un archivo saludo.txt
    with open("saludo.txt", "w") as archivo