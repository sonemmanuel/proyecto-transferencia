# ============================================================================
# MENÚ PRINCIPAL - Integración de todos los ejercicios (a1.py a a6.py)
# ============================================================================

from a1 import menu_promedio
from a2 import menu_contar_lineas
from a3 import menu_dividir_y_archivos
from a4 import menu_calculadora
from a5 import menu_validador_contrasena
from a6 import menu_procesamiento_ventas


def mostrar_menu_principal():
    """Muestra el menú principal con todas las opciones."""
    print("\n" + "=" * 70)
    print("MENÚ PRINCIPAL - EJERCICIOS DE PYTHON")
    print("=" * 70)
    print("1. Ejercicio 1: Calcular promedio de números")
    print("2. Ejercicio 2: Contar líneas de un archivo")
    print("3. Ejercicio 3: Dividir números y abrir archivo")
    print("4. Ejercicio 4: Calculadora refactorizada")
    print("5. Ejercicio 5: Validador de contraseñas")
    print("6. Ejercicio 6: Procesamiento de ventas")
    print("0. SALIR")
    print("=" * 70)


def ejecutar_menu(opcion):
    """Ejecuta el menú correspondiente según la opción seleccionada."""
    if opcion == "1":
        print("\n--- EJERCICIO 1: Promedio de Números ---")
        menu_promedio()
    elif opcion == "2":
        print("\n--- EJERCICIO 2: Contar Líneas de Archivo ---")
        menu_contar_lineas()
    elif opcion == "3":
        print("\n--- EJERCICIO 3: Dividir y Abrir Archivo ---")
        menu_dividir_y_archivos()
    elif opcion == "4":
        print("\n--- EJERCICIO 4: Calculadora ---")
        menu_calculadora()
    elif opcion == "5":
        print("\n--- EJERCICIO 5: Validador de Contraseñas ---")
        menu_validador_contrasena()
    elif opcion == "6":
        print("\n--- EJERCICIO 6: Procesamiento de Ventas ---")
        menu_procesamiento_ventas()
    elif opcion == "0":
        print("\n¡Hasta luego! 👋")
        return False
    else:
        print("\n❌ Opción no válida. Por favor, seleccione una opción válida.")
    return True


def main():
    """Función principal del menú."""
    while True:
        mostrar_menu_principal()
        opcion = input("Seleccione una opción: ").strip()
        if not ejecutar_menu(opcion):
            break


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Programa cancelado por el usuario.")
    except Exception as e:
        print(f"\n❌ Error inesperado: {e}")
