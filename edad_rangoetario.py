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