import os
import pandas as pd
import pydicom
import logging
import numpy as np

# Configurar el registro
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s') 
def listar_contenido_carpeta(ruta):
    """Lista el contenido de una carpeta, cuenta la cantidad de elementos y los imprime."""
    try:
        contenido = os.listdir(ruta)
        print(f"Contenido de la carpeta '{ruta}': {contenido}")
        print(f"Cantidad de elementos: {len(contenido)}")
    except FileNotFoundError:
        logging.error(f"La carpeta '{ruta}' no existe.")
    except Exception as e:
        logging.error(f"Error al listar el contenido de la carpeta: {e}")

def leer_archivo_csv(ruta, nombre_archivo):
    """Lee un archivo CSV y muestra información sobre el mismo."""
    try:
        ruta_completa = os.path.join(ruta, nombre_archivo)
        if not ruta_completa.endswith('.csv'):
            raise ValueError("El archivo proporcionado no es un archivo CSV")
        
        df = pd.read_csv(ruta_completa)
        print(f"Número de columnas: {len(df.columns)}")# Imprime número de columnas 
        print(f"Nombre de las columnas: {list(df.columns)}")# Imprime nombre de columnas 
        print(f"Número de filas: {len(df)}")# Imprime número de filas

# Calcula y muestra promedio y la desviación estándar de columnas numéricas        
        columnas_numericas = df.select_dtypes(include=[np.number])
        if not columnas_numericas.empty:
            print("\nPromedio por columna numérica:")
            print(columnas_numericas.mean())
            print("\nDesviación estándar por columna numérica:")
            print(columnas_numericas.std())
        else:
            raise ValueError("No hay columnas numéricas en el archivo CSV.")
    except FileNotFoundError:
        logging.error(f"El archivo '{nombre_archivo}' no se encontró en la ruta '{ruta}'.")
    except ValueError as ve:
        logging.error(ve)
    except Exception as e:
        logging.error(f"Error al leer el archivo CSV: {e}")


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

# Uso de las funciones
if __name__ == "__main__":
    listar_contenido_carpeta('./')# Listar contenido de una carpeta
    leer_archivo_csv('./', 'sample-01-csv.csv')# Leer archivo CSV
    leer_archivo_dicom('./', 'sample-01-dicom.dcm', '0x0010,0x0010', '0x0008,0x1030', '0x0008, 0x0016')# Leer archivo DICOM
    