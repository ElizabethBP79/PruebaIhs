from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import DICOMFile, MedicalImageResult
from .serializers import MedicalImageResultSerializer
from django.http import HttpResponse
from django.shortcuts import render
from .forms import DICOMFileForm
from .utils import process_dicom_file, leer_archivo_dicom

@api_view(["GET", "POST"])
def home(request):
    if request.method == 'GET':
        return HttpResponse("Welcome to the home page!")
    else:
        return HttpResponse("Method not allowed", status=405)

def upload_dicom(request):
    if request.method == 'POST':
        form = DICOMFileForm(request.POST, request.FILES)
        if form.is_valid():
            dicom_file = form.save()
            
            # Procesar el archivo DICOM
            processed_data = process_dicom_file(dicom_file.file)
            
            # Leer información adicional del archivo DICOM
            dicom_info = leer_archivo_dicom(dicom_file.file.path, dicom_file.file.name, 'PatientName', 'StudyDate', 'Modality')

            # Guardar los resultados en la base de datos
            medical_image_result = MedicalImageResult(
                device_name=processed_data["device_name"],
                raw_data=processed_data["raw_data"],
                average_before_normalization=processed_data["average_before_normalization"],
                average_after_normalization=processed_data["average_after_normalization"],
                data_size=processed_data["data_size"]
            )
            medical_image_result.save()
            
            return render(request, 'upload/upload.html', {'form': form, 'success': True})
    else:
        form = DICOMFileForm()

    return render(request, 'upload/upload.html', {'form': form})

class MedicalImageResultViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MedicalImageResult.objects.all()
    serializer_class = MedicalImageResultSerializer
    permission_classes = [IsAuthenticated]

@api_view(['GET'])
def get_image_results(request):
    results = MedicalImageResult.objects.all()
    serializer = MedicalImageResultSerializer(results, many=True)
    return Response(serializer.data)