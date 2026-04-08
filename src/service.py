from validate import validate_user, users

def new_register():
    print("Creando un nuevo registro...")
    username, _ = validate_user()
    if username is not None:
        print(f"Usuario '{username}' creado exitosamente.")
        return True
    else:
        print("Error al crear el usuario.")
        return False

# Uso de lambda para ordenar o buscar usuarios
def list_records():
    print("Listando registros...")
    if not users:
        print("No hay usuarios registrados.")
        return

    sorted_users = sorted(users, key=lambda x: x['name'])
    for user in sorted_users:
        print(f" \n ID: {user['id']}, Nombre: {user['name']}, Correo: {user['email']}, Edad: {user['age']}, Estado: {user['status']}")

def search_records():
    print("Buscando registros...")
    if not users:
        print("No hay usuarios registrados.")
        return

    search_name = input("Ingrese el nombre del usuario a buscar: ")
    found_users = list(filter(lambda u: u['name'].lower() == search_name.lower(), users))
    

    if found_users:
        for user in found_users:
            print(f" \n ID: {user['id']}, Nombre: {user['name']}, Correo: {user['email']}, Edad: {user['age']}, Estado: {user['status']} \n")
    else:
        print("No se encontraron usuarios con ese nombre.")

def update_record():
    print("Actualizando un registro...")
    try:
        print("Usuarios disponibles:")
        for user in users:
            print(f" \n ID: {user['id']}, Nombre: {user['name']}, Correo: {user['email']}, Edad: {user['age']}, Estado: {user['status']} \n")
            
        if not users:
            print("No hay usuarios registrados.")
            return
            
        user_id = int(input("Ingrese el ID del usuario a actualizar: "))
        user = next((u for u in users if u['id'] == user_id), None)
        if user is None:
            print("Usuario no encontrado.")
            return
        print(f"Actualizando usuario '{user['name']}' (ID: {user_id})")
        new_name = str(input("Ingrese el nuevo nombre (deje en blanco para mantener el actual): "))
        new_email = str(input("Ingrese el nuevo correo (deje en blanco para mantener el actual): "))
        new_status = str(input("Ingrese el nuevo estado (activo/inactivo, deje en blanco para mantener el actual): "))
        new_age = int(input("Ingrese la nueva edad (deje en blanco para mantener la actual): "))
        if new_name:
            user['name'] = new_name
        if new_email:
            user['email'] = new_email
        if new_status in ["activo", "inactivo"]:
            user['status'] = new_status
        if new_age:
            try:
                user['age'] = int(new_age)
            except ValueError:
                print("Edad inválida. Manteniendo la edad actual.")
        print(f"Usuario '{user['name']}' actualizado exitosamente.")
    except Exception as e:
        print(f"Error al actualizar el registro: {e}")

def delete_record():
    print("Eliminando un registro...")
    if not users:
        print("No hay usuarios registrados.")
        return

    try:
        print("Usuarios encontrados:")
        for u in users:
            print(f" \n ID: {u['id']}, Nombre: {u['name']}, Correo: {u['email']}, Edad: {u['age']}, Estado: {u['status']} \n")
            
        user_id = int(input("Ingrese el ID del usuario a eliminar: "))
        user = next((u for u in users if u['id'] == user_id), None)

        if user is None:
            print("Usuario no encontrado.")
            return

        users.remove(user)
        print(f"Usuario '{user['name']}' eliminado exitosamente.")
    except ValueError:
        print("ID inválido. Por favor, ingrese un número válido.")