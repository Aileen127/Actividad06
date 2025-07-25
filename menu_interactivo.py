

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
    for n in numero:
        if n > 0:
            positivo += 1


        elif n < 0:
            negativo += 1

    print(f"Hay {positivo}  números positivos")
    print(f"Hay {negativo} números negativos")

def area_triangulo(altura,base):
    return (altura * base) / 2

def verificar_par_impar(num):
        return num % 2 == 0

def calcular_promedio(calificacion):
    suma_calificacion = 0
    for c in calificacion:
        if calificacion != 0:
            suma_calificacion += c
            promedio = suma_calificacion / len(calificaciones)
    return promedio

def mayor_menor(lista_numeros):
    if lista_numeros:
        maximo =  max(lista_numeros)
        minimo = min(lista_numeros)
        print(f"El numero máximo en la lista es {maximo}")
        print(f"El numero máximo en la lista es {minimo}")

    else:
        print("La lista esta vacia.")








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
                numero = float(input("Ingresa los números que deseas evaluar, ingresa 0 si ya NO deseas ingresar más números: "))
                if numero != 0:
                    numeros.append(numero)
                elif numero == 0:
                    break

            print(f"La suma total es de: {suma_total(numeros)}")
            print(f"El promedio total es de: {promedio(numeros)}")
            cantidad_positivos_negativos(numeros)


        case "2":
            altura = float(input("Ingresa la altura del triangulo"))
            base = float(input("Ingresa la base del triangulo"))
            print(f"El area del triangulo es de: {area_triangulo(altura,base)}")

        case "3":
            num = int(input("Ingresa un número para verificar si es impar o par: "))
            if verificar_par_impar(num):
                print("El número es par.")
            else:
                print("El número es impar.")

        case "4":
            calificaciones = []
            while True:
                calificacion = float(input("Ingresa los calificaciones que deseas evaluar, ingresa 0 si ya NO deseas ingresar más opciones: "))
                if calificacion != 0:
                    calificaciones.append(calificacion)
                elif calificacion == 0:
                    break
                print(f"El promedio es de {calcular_promedio(calificaciones)}")

        case "5":
            lista_numeros = []
            while True:
                numero = int(input("Ingresa un numero, si ya no deseas agregar más ingresa 0: "))
                if numero != 0:
                    lista_numeros.append(numero)
                elif numero == 0:
                    break

            mayor_menor(lista_numeros)

        case "6":
            break