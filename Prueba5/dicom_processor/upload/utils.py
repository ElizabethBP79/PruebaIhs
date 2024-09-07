import pydicom
from io import BytesIO
import logging
import os
def process_dicom_file(file):
    # Leer el archivo DICOM usando pydicom
    dicom_data = pydicom.dcmread(BytesIO(file.read()))
    
    # Ejemplo de cómo obtener algunos datos del archivo DICOM
    device_name = dicom_data.get("Manufacturer", "Unknown Device")
    raw_data = dicom_data.pixel_array.tobytes()
    
    # Calcular valores de ejemplo (estos cálculos dependen de tu caso de uso específico)
    average_before_normalization = dicom_data.pixel_array.mean()
    average_after_normalization = dicom_data.pixel_array.max()  # Ejemplo de cálculo
    data_size = file.size
    
    return {
        "device_name": device_name,
        "raw_data": raw_data,
        "average_before_normalization": average_before_normalization,
        "average_after_normalization": average_after_normalization,
        "data_size": data_size
    }
def leer_archivo_dicom(ruta, nombre_archivo, *tags):
    """Lee un archivo DICOM e imprime la información del paciente, fecha del estudio, modalidad, y otros tags opcionales."""
    try:
        ruta_completa = os.path.join(ruta, nombre_archivo)
        ds = pydicom.dcmread(ruta_completa)

        # Imprimir información básica del paciente
        print(f"Nombre del paciente: {ds.PatientName}")
        print(f"Fecha del estudio: {ds.StudyDate}")
        print(f"Modalidad: {ds.Modality}")

        # Imprimir los tags opcionales proporcionados
        for tag in tags:
            try:
                tag_value = ds[tag].value
                print(f"Valor para el tag {tag}: {tag_value}")
            except KeyError:
                logging.warning(f"Tag {tag} no encontrado en el archivo DICOM.")
    except FileNotFoundError:
        logging.error(f"El archivo '{nombre_archivo}' no se encontró en la ruta '{ruta}'.")
    except pydicom.errors.InvalidDicomError:
        logging.error(f"El archivo '{nombre_archivo}' no es un archivo DICOM válido.")
    except Exception as e:
        logging.error(f"Error al leer el archivo DICOM: {e}")
