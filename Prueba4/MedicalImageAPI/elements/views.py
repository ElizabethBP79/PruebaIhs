from rest_framework import generics
from .models import MedicalImageResult
from .serializers import MedicalImageResultSerializer

class MedicalImageResultListCreate(generics.ListCreateAPIView):
    queryset = MedicalImageResult.objects.all()
    serializer_class = MedicalImageResultSerializer

class MedicalImageResultRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = MedicalImageResult.objects.all()
    serializer_class = MedicalImageResultSerializer