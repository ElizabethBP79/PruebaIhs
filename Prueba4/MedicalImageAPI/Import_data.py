import json
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MedicalImageAPI.settings")
django.setup()

from elements.models import MedicalImageResult

def load_data_from_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        print(f"Loaded data: {data}")  # Imprime los datos para verificar el formato

        # Recorre el diccionario y procesa cada ítem
        for key, item in data.items():
            if isinstance(item, dict):  # Verifica si cada ítem es un diccionario
                MedicalImageResult.objects.create(
                    id=item.get('id'),
                    device_name=item.get('deviceName'),
                    raw_data=item.get('data'),
                    average_before_normalization=0.0,  # Ajusta según tu archivo JSON
                    average_after_normalization=0.0,   # Ajusta según tu archivo JSON
                    data_size=len(item.get('data', []))  # Calcula el tamaño de los datos
                )
            else:
                print(f"Item is not a dictionary: {item}")

if __name__ == "__main__":
    load_data_from_json('./sample-04-json.json')