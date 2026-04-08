import validate
from service import new_register, list_records, search_records, update_record, delete_record
from file import load_data, save_data

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


while True:
    print("\nMenú de Gestión de Usuarios")
    print("1. Crear usuario")
    print("2. Listar registros")
    print("3. Buscar registros")
    print("4. Actualizar usuario")
    print("5. Eliminar usuario")
    print("6. Guardar datos")
    print("7. Salir")

    option = input("Seleccione una opción: ")

    if option == "1":
        user_created = new_register()
        if user_created:
            print("Usuario creado en memoria. Use la opción 6 para guardarlo en el archivo JSON.")
        else:
            print("No se pudo crear el usuario.")
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
            print("Datos guardados correctamente.")
        else:
            print("No se pudieron guardar los datos.")
    elif option == "7":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción del menú.")