edad = int(input("ingrese su edad "))
mayoria_edad = 18

if edad >= mayoria_edad:
	print("es mayor de edad")
else:
    print("es menor de edad")

''''''''''''

peso =  float(input("Ingrese su peso en kilogramos (kg): "))
talla = float(input("Ingrese su talla en metros (m): "))
imc = peso / (talla ** 2)
print(f"Su IMC es: {imc:.2f}")
if imc < 18.5:
    print("Clasificación: Bajo peso")
elif 18.5 <= imc < 24.9:
    print("Clasificación: Normal")
elif 25 <= imc < 29.9:
    print("Clasificación: Sobrepeso")
else:
    print("Clasificación: Obesidad")

''''''''''''
edad = int(input("Ingrese su edad: "))

if edad < 0:
    print("Edad no válida.")
elif edad <= 12:
    print("Rango etario: Niño/a")
elif edad <= 17:
    print("Rango etario: Adolescente")
elif edad <= 29:
    print("Rango etario: Joven adulto")
elif edad <= 59:
    print("Rango etario: Adulto")
else:
    print("Rango etario: Adulto mayor")

''''''''''''''

numero = int(input("Introduce un número entero: "))

if numero % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")

''''''''''''''

numero1 = float(input("ingrese el primer numero:"))
numero2 = float(input("ingresa el segundo numero:"))
print("\n ¿que desea hacer con estos numeros?")
print("1. sumar")
print("2. restar")
print("3. multiplicar")
print("4. dividir")
opcion = input("seleccione una opcion(1/2/3/4):")
if opcion == "1":
    resultado = numero1 + numero2
    print(f"resultado: {numero1} + {numero2} = {resultado}")
elif opcion == "2":
    resultado = numero1 - numero2
    print(f"Resultado: {numero1} - {numero2} = {resultado}")
elif opcion == "3":
    resultado = numero1 * numero2
    print(f"Resultado: {numero1} * {numero2} = {resultado}")
elif opcion == "4":
    if numero1 != 0:
        resultado = numero1 / numero2
        print(f"Resultado: {numero1} / {numero2} = {resultado}")
    else:
        print("Error: No se puede dividir entre cero.")
else:
    print("Opción no válida.")







