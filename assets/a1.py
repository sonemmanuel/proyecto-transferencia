#Leer numeros enteros separados por comas, calcular el promedio y manejar errores de conversion. COrrige ademas el calculo logico del promedio

try:
    numeros_str = input("Ingrese números enteros separados por comas: ")
    numeros = [int(num.strip()) for num in numeros_str.split(",")]
    
    if len(numeros) == 0:
        raise ValueError("No se ingresaron números.")
    else:
        suma = sum(numeros)
        cantidad = len(numeros)
        print(f"El resultado del promedio es: {suma / cantidad}")
    
except ValueError as e:
    print(f"Error de valor: {e}")
    
