
# Pedir dos números al usuario
num1 = float(input("Ingrese el primer número: 10"))
num2 = float(input("Ingrese el segundo número: 5"))

# Suma
suma = num1 + num2

# Resta
resta = num1 - num2

# Multiplicación
multiplicacion = num1 * num2

# División
if num2 != 0:
    division = num1 / num2
    modulo = num1 % num2
else:
    division = "No se puede dividir entre 0"
    modulo = "No se puede calcular módulo con 0"

# Mostrar resultados
print("Suma:15", suma)
print("Resta:5", resta)
print("Multiplicación:50", multiplicacion)
print("División:2.0", division)
print("Módulo:0", modulo)