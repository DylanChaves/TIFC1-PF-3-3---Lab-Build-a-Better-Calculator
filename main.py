
# Suma todos los números de una lista.
def addmultiplenumbers(numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    return resultado


# Multiplica todos los números de una lista.
def multiplymultiplenumbers(numeros):
    resultado = 1
    for numero in numeros:
        resultado *= numero
    return resultado


# Comprueba si el número es entero, aunque esté escrito como 3.0.
def isitaninteger(numero):
    return numero % 1 == 0


# Comprueba si el número es entero y par.
def isiteven(numero):
    return isitaninteger(numero) and numero % 2 == 0


# Solicita varios números separados por espacios.
def pedir_numeros():
    while True:
        try:
            entrada = input("Ingrese los números separados por espacios: ")
            numeros = [float(valor) for valor in entrada.split()]

            if numeros:
                return numeros

            print("Debe ingresar al menos un número.")
        except ValueError:
            print("Ingrese solo números. Use punto para los decimales.")


#  Impresion del menu
def main():
   while True:
        print("\n--- CALCULADORA ---")
        print("1. Sumar varios números")
        print("2. Multiplicar varios números")
        print("3. Comprobar si un número es par")
        print("4. Comprobar si un número es entero")
        print("0. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "0":
            print("¡Hasta luego!")
            break

        if opcion == "1":
            numeros = pedir_numeros()
            print("La suma es:", addmultiplenumbers(numeros))

        elif opcion == "2":
            numeros = pedir_numeros()
            print("La multiplicación es:", multiplymultiplenumbers(numeros))

        elif opcion in ("3", "4"):
            try:
                numero = float(input("Ingrese un número: "))

                if opcion == "3":
                    if isiteven(numero):
                        print("El número es par.")
                    else:
                        print("El número no es un entero par.")
                else:
                    if isitaninteger(numero):
                        print("El número es entero.")
                    else:
                        print("El número no es entero.")

            except ValueError:
                print("Entrada inválida. Debe ingresar un número.")

        else:
            print("Opción inválida. Seleccione una opción del menú.")


if __name__=="__main__":
  main()