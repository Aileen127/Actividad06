

# Definicion de funciones

def suma_total(numero):
    suma = 0
    for n in numero:
        if numero != 0:
            suma += n
    return suma

def promedio(numero):
        return sum(numero) / len(numero)

def cantidad_positivos_negativos(numero):
    positivo=0
    negativo=0
    for n in range(numero):
        if n > 0:
            positivo += 1
            print(f"Hay {positivo}  números positivos")

        elif n < 0:
            negativo += 1
            print(f"Hay {negativo} números negativos")






    else:
        print("Ingresa un dato valido por favor")





# Menu interactivo
while True:
    print("\n Bienvenido al menú")
    print("1. Ingresa n números para mostrar \n 1. Suma total \n 2. Promedio "
          "\n Cantidad de negativos y positivos")
    print("2. Calcular el área de un triángulo")
    print("3. Verificar si un número es par o impar")
    print("4. Calcular el promedio de n calificaciones")
    print("5. Ingresar n números y mostrar el mayor y el menor")
    print("6. Salir del programa")

    option = input("Ingresa una opción por favor (1 - 6): ")

    match option:
        case "1":
            numeros = []
            while True:
                numero = int(input("Ingresa los números que deseas evaluar, ingresa 0 si ya NO deseas ingresar más números: "))
                if numero != 0:
                    numeros.append(numero)
                elif numero == 0:
                    break
            print(f"La suma total es de: {suma_total(numeros)}")


        case "6":
            break