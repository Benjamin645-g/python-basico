print("menu")
print("1 iniciar partida")
print("2 nueva partida")
print("3 salir del juego")
opcion = int(input("ingrese su opcion "))


match opcion:
        case 1:
            print ("iniciar partida")
        case 2:
            print ("nueva partida")
        case 3:
            print ("salir del juego")
        case _:
            print ("su opcion no es valida")


'''
JAVASCRIPT

console.log("menu")
console.log("1 iniciar partida")
console.log("2 nueva partida")
console.log("3 salir del juego")
opcion = prompt("ingrese su opcion ")
console.log(opcion)

switch(opcion) {
    case "1":
        console.log("iniciar partida");
        break;
    case "2":
        console.log("nueva partida");
        break;
    case "3":
        console.log("salir del juego");
        break;
    default:
        console.log("su opcion no es valida")
}

'''