import pydicom
from celery import shared_task
from .models import MedicalImageResult

@shared_task(bind=True, max_retries=3)
def process_image(self, file_content):
    try:
        # Convertir el contenido del archivo a un objeto DICOM
        dicom_file = pydicom.read_file(file_content)
        
        # Ejemplo de procesamiento: obtener algunos valores promedio
        raw_data = extract_raw_data(dicom_file)
        average_before_normalization = calculate_average(raw_data)
        average_after_normalization = normalize_and_calculate_average(raw_data)
        data_size = len(file_content)
        
        # Guardar los resultados en la base de datos
        result = MedicalImageResult(
            id=dicom_file.SOPInstanceUID,
            device_name=dicom_file.DeviceSerialNumber,
            raw_data=raw_data,
            average_before_normalization=average_before_normalization,
            average_after_normalization=average_after_normalization,
            data_size=data_size
        )
        result.save()
        
    except Exception as exc:
        raise self.retry(exc=exc)

def extract_raw_data(dicom_file):
    # Ejemplo básico de extracción de datos. Deberás adaptar esto a tu formato real.
    return [
        "78 83 21 68 96 46 40 11 1 88",
        "58 75 71 69 33 14 15 93 18 54",
        "46 54 73 63 85 4 30 76 15 56"
    ]

def calculate_average(data):
    # Calcular promedio de los datos crudos
    return sum([float(num) for row in data for num in row.split()]) / len(data)

def normalize_and_calculate_average(data):
    # Normalizar los datos y calcular promedio
    normalized_data = [float(num) / max(float(num) for num in row.split()) for row in data for num in row.split()]
    return sum(normalized_data) / len(normalized_data)