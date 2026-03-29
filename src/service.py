from validate import validate_user, users

def create_user():
    print("Creando un nuevo usuario...")
    username, _ = validate_user()
    return username is not None


def list_users():
    print("Listando usuarios...")
    if not users:
        print("No hay usuarios registrados.")
        return

    for user in users:
        print(f" \n ID: {user['id']}, Nombre: {user['name']}, Correo: {user['email']}, Edad: {user['age']}, Estado: {user['status']}")
        
