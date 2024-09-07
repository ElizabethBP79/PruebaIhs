import logging
import pydicom

# Configuración del logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PatientRecord:
    """Clase para almacenar información del paciente."""
    def __init__(self, nombre, edad, fecha_nacimiento, sexo, peso, id_paciente, tipo_id):
        self.nombre = nombre
        self.edad = edad
        self.fecha_nacimiento = fecha_nacimiento
        self.sexo = sexo
        self.peso = peso
        self.id_paciente = id_paciente
        self.tipo_id = tipo_id
        self.diagnosis = None
    
    # Métodos para obtener la información del paciente
    def get_nombre(self):
        return self.nombre
    
    def get_edad(self):
        return self.edad

    def get_fecha_nacimiento(self):
        return self.fecha_nacimiento

    def get_sexo(self):
        return self.sexo

    def get_peso(self):
        return self.peso

    def get_id_paciente(self):
        return self.id_paciente

    def get_tipo_id(self):
        return self.tipo_id

    def get_diagnosis(self):
        return self.diagnosis

    # Métodos para establecer información del paciente
    def set_diagnosis(self, diagnosis):
        self.diagnosis = diagnosis

    # Método para actualizar el diagnóstico
    def update_diagnosis(self, new_diagnosis):
        self.diagnosis = new_diagnosis
        logging.info(f"El diagnóstico del paciente {self.id_paciente} ha sido actualizado a: {new_diagnosis}")
    
    def __str__(self):
        return (f"Nombre: {self.nombre}, Edad: {self.edad}, Fecha de Nacimiento: {self.fecha_nacimiento}, "
                f"Sexo: {self.sexo}, Peso: {self.peso}, ID del Paciente: {self.id_paciente}, Tipo de ID: {self.tipo_id}, "
                f"Diagnóstico: {self.diagnosis}")

class StudyRecord(PatientRecord):
    """Clase para almacenar información del estudio y detalles del paciente."""
    
    def __init__(self, nombre, edad, fecha_nacimiento, sexo, peso, id_paciente, tipo_id):
        super().__init__(nombre, edad, fecha_nacimiento, sexo, peso, id_paciente, tipo_id)
        self.modalidad = None
        self.fecha_estudio = None
        self.hora_estudio = None
        self.study_instance_uid = None
        self.numero_serie = None
        self.numero_cuadros = None

    # Métodos para establecer información del estudio
    def set_modalidad(self, modalidad):
        self.modalidad = modalidad

    def set_fecha_estudio(self, fecha):
        self.fecha_estudio = fecha

    def set_hora_estudio(self, hora):
        self.hora_estudio = hora

    def set_study_instance_uid(self, uid):
        self.study_instance_uid = uid

    def set_numero_serie(self, numero_serie):
        self.numero_serie = numero_serie

    def set_numero_cuadros(self, numero_cuadros):
        self.numero_cuadros = numero_cuadros

    # Método para cargar detalles del estudio desde un archivo DICOM
    def cargar_detalles_estudio_dicom(self, archivo_dicom):
        try:
            ds = pydicom.dcmread(archivo_dicom)
            logging.info(f"Archivo DICOM {archivo_dicom} leído exitosamente.\n")
            self.modalidad = ds.Modality
            self.fecha_estudio = ds.StudyDate
            self.hora_estudio = ds.StudyTime
            self.study_instance_uid = ds.StudyInstanceUID
            self.numero_serie = ds.SeriesNumber
            self.numero_cuadros = getattr(ds, 'NumberOfFrames', 'No especificado')
        except Exception as e:
            logging.error(f"Error al cargar detalles del estudio desde el archivo DICOM: {e}\n")
    
    def __str__(self):
        return (f"Información del Paciente:\n\n"
                f" - Nombre: {self.nombre}\n"
                f" - Edad: {self.edad}\n"
                f" - Fecha de Nacimiento: {self.fecha_nacimiento}\n"
                f" - Sexo: {self.sexo}\n"
                f" - Peso: {self.peso}\n"
                f" - ID del Paciente: {self.id_paciente}\n"
                f" - Tipo de ID: {self.tipo_id}\n"
                f" - Diagnóstico: {self.diagnosis}\n\n"
                f"Información del Estudio:\n\n"
                f" - Modalidad: {self.modalidad}\n"
                f" - Fecha del Estudio: {self.fecha_estudio}\n"
                f" - Hora del Estudio: {self.hora_estudio}\n"
                f" - UID de la Instancia del Estudio: {self.study_instance_uid}\n"
                f" - Número de Serie: {self.numero_serie}\n"
                f" - Número de Cuadros: {self.numero_cuadros}")
    


if __name__ == "__main__":
    # Crear una instancia de StudyRecord
    paciente = StudyRecord("Juan Penagos", 23, "2000-10-12", "M", 92, "12345", "DNI")
    print(paciente)

    # Actualizar diagnóstico del paciente
    paciente.update_diagnosis("Hipertensión")

    # Cargar detalles del estudio desde un archivo DICOM
    paciente.cargar_detalles_estudio_dicom('./sample-02-dicom.dcm')

    # Imprimir toda la información del paciente y del estudio
    print(paciente)
