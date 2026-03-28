from validate import validate_status, validate_age, validate_email, validate_user, users

def create_user():
    print("Creando un nuevo usuario...")
    validate_user()


def list_users():
    print("Listando usuarios...")
    for user in users:
        print(f" \n ID: {user['id']}, Nombre: {user['name']}, Correo: {user['email']}, Edad: {user['age']}, Estado: {user['status']}"