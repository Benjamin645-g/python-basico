num1= float(input("ingrese el primer numero:"))
num2= float(input("ingrese el segundo numero:"))
print("¿que desea hacer con estos numero?")
print("1. sumar")
print("2. restar")
print("3. multiplicar")
print("4. dividir")
opcion=(" \n ingrese el numero de la opcion:")
if opcion == '1':
    resultado = num1 + num2
    print("La suma es:", resultado)
elif opcion == '2':
    resultado = num1 - num2
    print("La resta es:", resultado)
elif opcion == '3':
    resultado = num1 * num2
    print("La multiplicación es:", resultado)
elif opcion == '4':
    if num2 != 0:
        resultado = num1 / num2
        print("La división es:", resultado)
    else:
        print("Error: no se puede dividir por cero.")
else:
    print("Opción no válida.")