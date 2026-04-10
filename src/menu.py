import validate
from service import new_register, list_records, search_records, update_record, delete_record
from file import load_data, save_data
from colorama import Fore, Style
from integration import export_to_csv, generate_report

def load_users_into_memory():
    """Sincroniza usuarios e id_counter desde el archivo JSON."""
    initial_users = load_data()
    validate.users.clear()
    validate.users.extend(initial_users)

    valid_ids = [
        user.get("id")
        for user in initial_users
        if isinstance(user, dict) and isinstance(user.get("id"), int)
    ]
    validate.id_counter = max(valid_ids) + 1 if valid_ids else 1


load_users_into_memory()


def main_menu():
    """Displays the main menu with color styling."""
    while True:
        print(f"\n{Fore.CYAN}{'='*40}")
        print(f"{Fore.CYAN}Menú de Gestión de Usuarios")
        print(f"{Fore.CYAN}{'='*40}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}1.{Style.RESET_ALL} Crear usuario")
        print(f"{Fore.YELLOW}2.{Style.RESET_ALL} Listar registros")
        print(f"{Fore.YELLOW}3.{Style.RESET_ALL} Buscar registros")
        print(f"{Fore.YELLOW}4.{Style.RESET_ALL} Actualizar usuario")
        print(f"{Fore.YELLOW}5.{Style.RESET_ALL} Eliminar usuario")
        print(f"{Fore.YELLOW}6.{Style.RESET_ALL} Guardar datos")
        print(f"{Fore.YELLOW}7.{Style.RESET_ALL} Generar Reporte")
        print(f"{Fore.YELLOW}8.{Style.RESET_ALL} Exportar a CSV")
        print(f"{Fore.RED}9.{Style.RESET_ALL} Salir")

        option = input(f"\n{Fore.GREEN}Seleccione una opción: {Style.RESET_ALL}")

        if option == "1":
            user_created = new_register()
            if user_created:
                print(f"{Fore.GREEN}✓ Usuario creado en memoria. Use la opción 6 para guardarlo en el archivo JSON.{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}✗ No se pudo crear el usuario.{Style.RESET_ALL}")
        elif option == "2":
            list_records()
        elif option == "3":
            search_records()
        elif option == "4":
            update_record()
        elif option == "5":
            delete_record()
        elif option == "6":
            if save_data(validate.users):
                print(f"{Fore.GREEN}✓ Datos guardados correctamente.{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}✗ No se pudieron guardar los datos.{Style.RESET_ALL}")
        elif option == "7":
            generate_report(validate.users)
        elif option == "8":
            export_to_csv(validate.users)
        elif option == "9":
            print(f"{Fore.CYAN}Saliendo del programa...{Style.RESET_ALL}")
            break
        else:
            print(f"{Fore.RED}✗ Opción inválida. Por favor, seleccione una opción del menú.{Style.RESET_ALL}")
main_menu()