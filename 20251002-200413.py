# Pedir los dos números al usuario
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

# Comparar los números
if num1 == num2:
    print("Los números son iguales.")
elif num1 > num2:
    print("El primer número es mayor que el segundo.")
else:
    print("El primer número es menor que el segundo.")