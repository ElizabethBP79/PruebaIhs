from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from upload.views import DICOMResultViewSet, upload_dicom

# Configurar el enrutador de la API
router = DefaultRouter()
router.register(r'dicom-results', DICOMResultViewSet, basename='dicomresult')

urlpatterns = [
    # Ruta para el panel de administración de Django
    path('admin/', admin.site.urls),

    # Ruta para la carga de archivos DICOM
    path('upload/', upload_dicom, name='upload_dicom'),

    # Rutas para los endpoints de resultados DICOM
    path('api/', include(router.urls)),
]