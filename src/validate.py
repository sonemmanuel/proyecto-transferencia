users = []
id_counter = 1

def validate_email():
    while True:
        try:
            email = "olivernie2626@gmail.com"
            if "@" in email and "." in email:
                print("Correo válido.")
                return email
        except ValueError:
            print("Por favor, ingrese un correo válido.")

def validate_age():
    while True:
        try:
            age = 18
            if age <= 0 or age >= 100:
                print("La edad no es válida. Ingrese una edad entre 1 y 99.")
            else:
                print("Edad válida")
                return age
        except ValueError:
            print("Por favor, ingrese un número válido.")
            
def validate_status():
    while True:
        try:
            status = "active"
            if status in ["active", "inactive"]:
                print("Estado válido.")
                return status
        except ValueError:
            print("Por favor, ingrese un estado válido.")

def validate_user():
    global id_counter
    try:
        print(f"Id de usuario asignado: {id_counter}")
        
        # Validate name
        username = "Oliver"
        
        # Validate email
        email = validate_email()
        
        # Validate age
        age = validate_age()
        
        # Validate status
        status = validate_status()
        
        # Create user with all information
        user = {
            "id": id_counter,
            "name": username,
            "email": email,
            "age": age,
            "status": status
        }
        users.append(user)
        
        assigned_id = id_counter
        id_counter += 1
        
        print(f"\nUsuario registrado: {username} (ID: {assigned_id}, Correo: {email}, Edad: {age}, Estado: {status})\n")
        return username, assigned_id
        
    except ValueError as e:
        print(f"Error de validación: {e}")
        return None, None
    except Exception as e:
        print(f"Error inesperado: {e}")
        return None, None