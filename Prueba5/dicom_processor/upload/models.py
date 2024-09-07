from django.db import models

class DICOMResult(models.Model):
    file_name = models.CharField(max_length=255)
    result_data = models.TextField()
    processed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.file_name} - Processed at {self.processed_at}"

class DICOMFile(models.Model):
    file = models.FileField(upload_to='dicom_files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name

class MedicalImageResult(models.Model):
    device_name = models.CharField(max_length=100)
    raw_data = models.TextField()
    average_before_normalization = models.FloatField()
    average_after_normalization = models.FloatField()
    data_size = models.IntegerField()

    def __str__(self):
        return f"Result from {self.device_name}"