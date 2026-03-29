import json
from pathlib import Path


DATA_FILE = (Path(__file__).resolve().parent / "../data/registros.json").resolve()


def load_data():
	"""Carga los registros desde JSON; si falla, retorna una lista vacia."""
	DATA_FILE.parent.mkdir(parents=True, exist_ok=True)

	if not DATA_FILE.exists():
		try:
			with DATA_FILE.open("w", encoding="utf-8") as file:
				json.dump([], file, ensure_ascii=False, indent=4)
		except OSError as error:
			print(f"Error al crear archivo de datos: {error}. Se usara lista vacia.")
		return []

	try:
		with DATA_FILE.open("r", encoding="utf-8") as file:
			raw_content = file.read().strip()

		if not raw_content:
			return []

		data = json.loads(raw_content)
		if isinstance(data, list):
			return data

		print("Advertencia: el archivo de datos no contiene una lista valida. Se usara lista vacia.")
		return []
	except json.JSONDecodeError:
		print("Error: el archivo de datos esta dañado o tiene formato invalido. Se usara lista vacia.")
		return []
	except OSError as error:
		print(f"Error al leer archivo de datos: {error}. Se usara lista vacia.")
		return []


def save_data(data):
	"""Guarda los registros en JSON de forma segura."""
	try:
		DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
		with DATA_FILE.open("w", encoding="utf-8") as file:
			json.dump(data, file, ensure_ascii=False, indent=4)
		return True
	except TypeError as error:
		print(f"Error: los datos no son serializables a JSON: {error}")
		return False
	except OSError as error:
		print(f"Error al guardar archivo de datos: {error}")
		return False