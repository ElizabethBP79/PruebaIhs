# from django.contrib import admin
# from .models import DICOMResult, DICOMFile  # Importa tus modelos

# @admin.register(DICOMResult)
# class DICOMResultAdmin(admin.ModelAdmin):
#     list_display = ('file_name', 'processed_at')  # Campos que se mostrarán en la lista de objetos
#     search_fields = ('file_name',)  # Campos que serán buscables en el panel de administración

# @admin.register(DICOMFile)
# class DICOMFileAdmin(admin.ModelAdmin):
#     list_display = ('file', 'uploaded_at')  # Campos que se mostrarán en la lista de objetos
#     search_fields = ('file',) 


from django.contrib import admin
from .models import DICOMResult, DICOMFile  # Importa tus modelos

# Cambia el nombre del panel de administración
admin.site.site_header = 'Sistema de procesamiento DICOM'
admin.site.site_title = 'Sistema de procesamiento DICOM'
admin.site.index_title = 'Bienvenido al panel de administración'

@admin.register(DICOMResult)
class DICOMResultAdmin(admin.ModelAdmin):
    list_display = ('file_name', 'processed_at')  # Campos que se mostrarán en la lista de objetos
    search_fields = ('file_name',)  # Campos que serán buscables en el panel de administración

@admin.register(DICOMFile)
class DICOMFileAdmin(admin.ModelAdmin):
    list_display = ('file', 'uploaded_at')  # Campos que se mostrarán en la lista de objetos
    search_fields = ('file',)