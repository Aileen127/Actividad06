

# Definicion de funciones

def ingreso_numeros():
    numeros = []
    numero = int(input("Ingresa la cantidad de números que deseas evaluar (digitos)"))

    if numero > 0:
        def suma_total(numero):
            suma = 0
            for n in numeros:
                suma += n
                print(f"EL total es de: {suma}")

        def promedio(numero):
            return sum(numeros) / len(numeros)




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
    print("5. INgresar n números y mostrar el mayor y el menor")
    print("6. Salir del programa")

    option = input("Ingresa una opción por favor (1 - 6)")

    match option:
        case "1":
            ingreso_numeros()

        case "6":
            break