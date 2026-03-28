# 🧩 Ejercicio 5: Refactorizar validador de contraseñas
# OBJETIVO: Función clara, nombres explícitos, retornos tempranos, fácil de extender

# REGLAS DE VALIDACIÓN
# 1. Longitud mínima 8
# 2. Debe tener al menos 1 dígito
# 3. Debe tener al menos 1 mayúscula
# 4. No puede contener espacios

# Validadores con lambdas (reglas simples y reutilizables)
has_min_length = lambda pwd: len(pwd) >= 8
has_no_spaces = lambda pwd: " " not in pwd
has_uppercase = lambda pwd: pwd != pwd.lower()
has_digits = lambda pwd: any(c.isdigit() for c in pwd)

# Función principal con nombres claros y retornos tempranos
def is_valid_password(password: str) -> bool:
    """
    Valida una contraseña según reglas de seguridad.
    
    Retorna True si es válida, False en caso contrario.
    """
    try:
        # Validar tipo
        if not isinstance(password, str):
            return False
        
        # Retornos tempranos: cada regla es independiente
        if not has_min_length(password):
            return False
        if not has_no_spaces(password):
            return False
        if not has_uppercase(password):
            return False
        if not has_digits(password):
            return False
        
        return True
    
    except Exception:
        return False


# PRUEBAS (mínimo 6)
if __name__ == "__main__":
    # test_cases = [
    #     ("Abcdefg1", True),
    #     ("abcdefg1", False),      # sin mayúscula
    #     ("ABCDEFGH", False),      # sin número
    #     ("Password123", True),
    #     ("Password", False),       # sin número
    #     ("password123", False),    # sin mayúscula
    # ]
    
    # print("=" * 50)
    # print("PRUEBAS: Validador de Contraseñas")
    # print("=" * 50)
    
    # passed = sum(1 for pwd, expected in test_cases if is_valid_password(pwd) == expected)
    
    # for pwd, expected in test_cases:
    #     result = is_valid_password(pwd)
    #     status = "✓ PASS" if result == expected else "✗ FAIL"
    #     print(f"{status}: '{pwd}' → {result}")
    
    # print("=" * 50)
    # print(f"Resultado: {passed}/{len(test_cases)} pruebas pasadas\n")
    
    try:
        pwd = input("Ingresa una contraseña para validar: ")
        result = is_valid_password(pwd)
        print(f"Resultado: {'✓ VÁLIDA' if result else '✗ INVÁLIDA'}")
    except KeyboardInterrupt:
        print("\nOperación cancelada")
    except Exception as e:
        print(f"Error: {e}")