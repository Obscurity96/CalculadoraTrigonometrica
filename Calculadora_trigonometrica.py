import math

def mostrar_menu():
    print("Seleccione la operación que desea realizar:")
    print("1. Seno")
    print("2. Coseno")
    print("3. Tangente")
    print("4. Cotangente")
    print("5. Secante")
    print("6. Cosecante")
    print("0. Salir")

def operacion_trigonometrica(opcion):
    if opcion == '1':
        angulo = float(input("Ingrese el ángulo en grados para calcular el seno: "))
        return math.sin(math.radians(angulo))
    elif opcion == '2':
        angulo = float(input("Ingrese el ángulo en grados para calcular el coseno: "))
        return math.cos(math.radians(angulo))
    elif opcion == '3':
        angulo = float(input("Ingrese el ángulo en grados para calcular la tangente: "))
        return math.tan(math.radians(angulo))
    elif opcion == '4':
        angulo = float(input("Ingrese el ángulo en grados para calcular la cotangente: "))
        return 1 / math.tan(math.radians(angulo))
    elif opcion == '5':
        angulo = float(input("Ingrese el ángulo en grados para calcular la secante: "))
        return 1 / math.cos(math.radians(angulo))
    elif opcion == '6':
        angulo = float(input("Ingrese el ángulo en grados para calcular la cosecante: "))
        return 1 / math.sin(math.radians(angulo))
    elif opcion == '0':
        print("Saliendo...")
        return None
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")

def main():
    while True:
        mostrar_menu()
        opcion = input("Ingrese el número de la operación deseada: ")
        
        if opcion == '0':
            break

        resultado = operacion_trigonometrica(opcion)
        if resultado is not None:
            print("El resultado es:", resultado)

if __name__ == "__main__":
    main()
