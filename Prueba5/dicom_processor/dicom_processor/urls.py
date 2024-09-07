from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from upload.views import MedicalImageResultViewSet, upload_dicom, home
from django.http import JsonResponse
# Configurar el enrutador de la API
router = DefaultRouter()
router.register(r'dicom-results', MedicalImageResultViewSet, basename='dicomresult')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload/', upload_dicom, name='upload_dicom'),
    path('api/', include(router.urls)),
    path('', home, name='home'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

print("Registered URL patterns:")
for url_pattern in urlpatterns:
    print(url_pattern)