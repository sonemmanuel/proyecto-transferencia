# # Ejercicio 4: 
# Analiza el siguiente “código existente” y realiza un -> refactor <-, tener en cuenta los 
# problemas que se plantean al final.

# Código original (difícil de mantener)

def calc(a, b, op):
    try:
        ops = {
            "suma": lambda x, y: x + y,
            "resta": lambda x, y: x - y,
            "multiplicacion": lambda x, y: x * y,
            "division": lambda x, y: x / y if y != 0 else (_ for _ in ()).throw(ZeroDivisionError("No se puede dividir entre cero."))
        }
        
        if op not in ops:
            raise ValueError(f"Operación '{op}' no válida.")
        
        func = ops[op]
        return func(a, b)
    
    except ZeroDivisionError as e:
        print(f"Error: {e}")
        return None
    except ValueError as e:
        print(f"Error: {e}")
        return None
    except Exception as e:
        print(f"Error inesperado: {e}")
        return None

try:
    a = int(input("Ingrese el primer número: "))
    b = int(input("Ingrese el segundo número: "))
    op = str(input("Ingrese la operación (suma, resta, multiplicacion, division): "))
    
    result = calc(a, b, op)
    if result is not None:
        print(f"El resultado de la {op} es: {result}")
except ValueError:
    print("Error: Ingrese números válidos.")
except Exception as e:
    print(f"Error: {e}")

# Problemas:
# • Retorna "error" (string) o números → mezcla de tipos (confuso)
# • op con letras “mágicas”
# • No deja claro qué errores existen
# • Difícil testear los errores bien