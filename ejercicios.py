lado = float(input("introduce el lado del cuadrado:"))
perimetro = 4*lado
area =  lado **2
print(f"el perimetro del cuadrado es: {perimetro}")
print(f"el area del cuadrado es{area}")

''''''''''''''''''''

lado1 = float(input("introduce el primer lado del rectangulo:"))
lado2 = float(input("introduce el segundo lado del rectangulo:"))
perimetro = 2* (lado1 + lado2)
area = lado1 * lado2
print(f"el perimetro del rectangulo es: {perimetro}")
print(f"el area del rectangulo es: {area}")

''''''''''''''''''''
pi = 3.14
radio = float(input("introduce el radio del circulo: "))
perimetro = 2 * pi * radio
area = pi * radio **2
print(f"el perimetro del circulo es: {perimetro}")
print(f"el area del circulo es: {area}")

''''''''''''''''''''
base = float(input("introduce la base del triangulo rectangulo:"))
altura = float(input("introduce la altura del triangulo rectangulo:"))
area = (base * altura) /2
print(f"el area del triangulo rectangulo es: {area}")

''''''''''''''''''''
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2

if num2 != 0:
    division = num1 / num2
else:
    division = "No se puede dividir entre cero."

print("\nResultados:")
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")

''''''''''''''''''''
numeros = []

for i in range(5):
    num = float(input(f"Ingrese el número {i + 1}: "))
    numeros.append(num)

promedio = sum(numeros) / len(numeros)

print(f"\nEl promedio de los 5 números es: {promedio}")

''''''''''''''''''''''''''
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

if num1 > num2:
    print(f"El número mayor es: {num1}")
elif num2 > num1:
    print(f"El número mayor es: {num2}")
else:
    print("Son iguales")


''''''''''''''''''''''''
radio = float(input("Ingresa el radio del círculo: "))
area = pi * (radio ** 2)
print(f"El área del círculo es: {area}")

''''''''''''''''''''''''

precio_original = float(input("Ingrese el precio original del producto: "))
tiene_descuento = input("¿El producto tiene descuento? (sí/no): ").strip().lower()
if tiene_descuento == "sí" or tiene_descuento == "si":

    precio_descuento = float(input("Ingrese el precio con descuento: "))
    
    descuento = ((precio_original - precio_descuento) / precio_original) * 100
    print(f"El porcentaje de descuento es: {descuento:.2f}%")
else:
    print("El producto no tiene descuento.")

''''''''''''''''''''
numero = int(input("Ingresa un número entre 1 y 1000: "))
if 1 <= numero <= 1000:
    if numero < 10:
        print("El número tiene 1 dígito.")
    elif numero < 100:
        print("El número tiene 2 dígitos.")
    elif numero < 1000:
        print("El número tiene 3 dígitos.")
    else: 
        print("El número tiene 4 dígitos.")
else:
    print("El número no está en el rango de 1 a 1000.")
