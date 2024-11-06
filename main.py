from sumar import sumar
from resta import resta
from multiplicacion import multiplicar
from dividir import dividir
from suma_avanzada import suma_avanzada

def mostrar_menu():
    print("Calculadora")
    print("1. Sumar dos números")
    print("2. Restar dos números")
    print("3. Multiplicar dos números")
    print("4. Dividir dos números")
    print("5. Sumar una cantidad de números")
    print("6. Salir")

def ejecutar_operacion(opcion):
    if opcion == 1:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        print(f"Resultado: {sumar(num1, num2)}")
    elif opcion == 2:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        print(f"Resultado: {resta(num1, num2)}")
    elif opcion == 3:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        print(f"Resultado: {multiplicar(num1, num2)}")
    elif opcion == 4:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        print(f"Resultado: {dividir(num1, num2)}")
    elif opcion == 5:
        n = int(input("Cuántos números deseas sumar? "))
        numeros = [float(input(f"Ingrese el número {i+1}: ")) for i in range(n)]
        print(f"Resultado: {suma_avanzada(numeros)}")
    elif opcion == 6:
        print("¡Adiós!")
        return False
    return True

def main():
    while True:
        mostrar_menu()
        opcion = int(input("Elige una opción: "))
        if not ejecutar_operacion(opcion):
            break

if __name__ == "__main__":
    main()
