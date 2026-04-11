import unittest  # Framework de testing
from unittest.mock import patch  # Herramienta para mockear funciones
import sys
import os

# Agregar el directorio padre al path de Python para poder importar desde src
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Importar los módulos a testear
from src import validate, service

# IMPORTANTE: Sincronizar la lista de usuarios entre service y validate
# Esto asegura que ambos módulos trabajen con el mismo objeto
import src.service as service_module
service_module.users = validate.users

# Clase que contiene todos los tests
class TestGestionInfo(unittest.TestCase):
    
    def setUp(self):
        """Se ejecuta antes de cada test para resetear el estado"""
        validate.users.clear()
        service_module.users = validate.users  # Sincronizar la referencia
        validate.id_counter = 1
    
    # Test 1: Crear un nuevo usuario con validaciones
    @patch('builtins.input', side_effect=['Juan Pérez', 'juan@test.com', '25', 'activo'])
    def test_1_crear_usuario(self, mock_input):
        """
        Testea la función validate_user() simulando inputs del usuario.
        side_effect proporciona valores secuenciales para cada input() como strings.
        """
        # Ejecutar la función a testear
        username, user_id = validate.validate_user()
        
        # Verificar que el usuario fue creado correctamente
        self.assertIsNotNone(username, "El nombre de usuario no debería ser None")
        self.assertEqual(username, 'Juan Pérez', "El nombre no coincide")
        self.assertEqual(user_id, 1, "El ID del usuario debería ser 1")
        
        # Verificar que exactamente 1 usuario fue agregado a la lista
        self.assertEqual(len(validate.users), 1, "Debería haber exactamente 1 usuario en la lista")
        
        # Verificar los detalles del usuario creado
        usuario = validate.users[0]
        self.assertEqual(usuario['id'], 1, "El ID no coincide")
        self.assertEqual(usuario['name'], 'Juan Pérez', "El nombre no coincide")
        self.assertEqual(usuario['email'], 'juan@test.com', "El email no coincide")
        self.assertEqual(usuario['age'], 25, "La edad no coincide")
        self.assertEqual(usuario['status'], 'activo', "El estado no coincide")

    
    # Test 2: Listar todos los usuarios registrados (después de crear uno)
    @patch('builtins.input', side_effect=['María García', 'maria@test.com', '30', 'activo'])
    def test_2_listar_usuarios(self, mock_input):
        """
        Testea la función list_records() que muestra todos los usuarios.
        Primero crea un usuario, luego lo lista y verifica que aparezca.
        """
        # Crear un usuario primero
        username, user_id = validate.validate_user()
        self.assertEqual(len(validate.users), 1, "Debería haber 1 usuario después de la creación")
        
        # Listar los usuarios (capturar la salida para verificar)
        with patch('builtins.print') as mock_print:
            service.list_records()
            # Verificar que se llamó a print (la función imprime los registros)
            self.assertTrue(mock_print.called, "list_records() debería haber impreso algo")
        
        # Verificar que el usuario sigue en la lista
        self.assertEqual(len(validate.users), 1, "Debería seguir habiendo 1 usuario")
        self.assertEqual(validate.users[0]['name'], 'María García', "El nombre del usuario no coincide")

        
    # Test 3: Eliminar un usuario de la lista
    def test_3_eliminar_usuario(self):
        """
        Testea la función delete_record() que remueve un usuario.
        Primero crea un usuario, luego lo elimina y verifica que fue removido.
        """
        # Crear un usuario primero con inputs simulados
        with patch('builtins.input', side_effect=['Pedro López', 'pedro@test.com', '35', 'inactivo']):
            username, user_id = validate.validate_user()
        
        self.assertEqual(len(validate.users), 1, "Debería haber 1 usuario después de la creación")
        
        usuario_id = validate.users[0]['id']
        
        # Eliminar el usuario con input para el ID
        with patch('builtins.input', side_effect=[str(usuario_id)]):
            with patch('builtins.print'):  # Suprime la salida de print
                service.delete_record()
        
        # Verificar que el usuario fue eliminado
        self.assertEqual(len(validate.users), 0, "No debería haber usuarios después de eliminar")
        
        # Verificar que ningún usuario tiene el ID que eliminamos
        usuarios_restantes = [u for u in validate.users if u['id'] == usuario_id]
        self.assertEqual(len(usuarios_restantes), 0, "El usuario eliminado no debería existir en la lista")


# Punto de entrada del script
if __name__ == '__main__':
    unittest.main()