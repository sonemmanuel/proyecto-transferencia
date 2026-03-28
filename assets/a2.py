#Abrir un archivo, capturar errores de apertura, contar lineas en else, cerrar en finally y mostrar un mensaje fianl

try:
    archivo = open("archivo.txt", "r", encoding="utf-8")
except Exception as e:
    print(f"Error: {e}")
else:
    lineas = archivo.readlines()
    print(f"El número de líneas en el archivo es: {len(lineas)}")
finally:
    try:
        archivo.close()
    except NameError:
        print("El archivo no se abrió, no se puede cerrar.")
    else:
        print("Archivo cerrado correctamente.")