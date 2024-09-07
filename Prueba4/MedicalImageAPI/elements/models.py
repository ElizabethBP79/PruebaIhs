from django.db import models
from django.db.models import JSONField

class MedicalImageResult(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    device_name = models.CharField(max_length=100)
    raw_data = JSONField()  # Usa django.db.models.JSONField
    average_before_normalization = models.FloatField()
    average_after_normalization = models.FloatField()
    data_size = models.IntegerField()

    def __str__(self):
        return f"{self.device_name} ({self.id})"