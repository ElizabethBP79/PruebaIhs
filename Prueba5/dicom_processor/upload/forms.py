from django import forms
from .models import DICOMFile

class DICOMFileForm(forms.ModelForm):
    class Meta:
        model = DICOMFile
        fields = ['file']
        widgets = {
            'file': forms.ClearableFileInput(attrs={'multiple': False}),}

    def clean_file(self):
        file = self.cleaned_data.get('file')
        # Validaciones adicionales para asegurarse de que el archivo sea DICOM
        # Ejemplo: Verificar extensión del archivo o contenido
        if not file.name.lower().endswith('.dcm'):
            raise forms.ValidationError("El archivo debe ser un archivo DICOM (.dcm).")
        return file 