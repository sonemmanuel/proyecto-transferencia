import validate
from service import create_user, list_users
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
    print("Menú de Gestión de Usuarios")
    print("1. Crear usuario")
    print("2. Listar usuarios")
    print("3. Guardar datos")
    print("4. Salir")

    option = input("Seleccione una opción: ")

    if option == "1":
        user_created = create_user()
        if user_created:
            print("Usuario creado en memoria. Use la opción 3 para guardarlo en el archivo JSON.")
        else:
            print("No se pudo crear el usuario.")
    elif option == "2":
        list_users()
    elif option == "3":
        if save_data(validate.users):
            print("Datos guardados correctamente.")
        else:
            print("No se pudieron guardar los datos.")
    elif option == "4":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción del menú.")