from service import create_user, list_users

while True:
    print("Menú de Gestión de Usuarios")
    print("1. Crear usuario")
    print("2. Listar usuarios")
    print("3. Salir")

    option = input("Seleccione una opción: ")

    if option == "1":
        create_user()
    elif option == "2":
        list_users()
    elif option == "3":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción del menú.")