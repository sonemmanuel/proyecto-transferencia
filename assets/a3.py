#Crear un menú con: (1) Dividir números, (2) abrir un archivo y mostrar primera linea, (3) salir.
#Capturar ValueError, ZeroDivisionError, FileNotFoundError y usa un except
#Exception final para no previstos

while True:
    print("Menú: ")
    print("1. Dividir números")
    print("2. Abrir un archivo y mostrar la primera línea")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        try:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            resultado = num1 / num2
            print(f"El resultado de la división es: {resultado}")
        except ValueError:
            print("Error: Por favor, ingrese números válidos.")
        except ZeroDivisionError:
            print("Error: No se puede dividir entre cero.")
    elif opcion == "2":
        try:
            archivo = open("archivo.txt", "r", encoding="utf-8")
        except FileNotFoundError:
            print("Error: El archivo no se encontró.")
        except Exception as e:
            print(f"Error: {e}")
        else:
            try:
                primera_linea = archivo.readline()
                print(f"La primera línea del archivo es: {primera_linea}")
            except Exception as e:
                print(f"Error: {e}")
            finally:
                try:
                    archivo.close()
                except NameError:
                    print("El archivo no se abrió, no se puede cerrar.")
    elif opcion == "3":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")