from django.urls import path
from .views import MedicalImageResultListCreate, MedicalImageResultRetrieveUpdateDelete

urlpatterns = [
    path('api/elementos/', MedicalImageResultListCreate.as_view(), name='elementos-list-create'),
    path('api/elementos/<str:pk>/', MedicalImageResultRetrieveUpdateDelete.as_view(), name='elementos-retrieve-update-delete'),
]
