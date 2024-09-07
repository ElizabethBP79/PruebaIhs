from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import DICOMFile, MedicalImageResult

class DICOMFileUploadTests(APITestCase):
    def test_upload_dicom_file(self):
        with open('path/to/testfile.dcm', 'rb') as file:
            response = self.client.post(reverse('upload_dicom'), {'file': file}, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], 'File uploaded and processing started.')

    def test_invalid_file_format(self):
        with open('path/to/invalidfile.txt', 'rb') as file:
            response = self.client.post(reverse('upload_dicom'), {'file': file}, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['error'], 'Invalid file format')

class MedicalImageResultTests(APITestCase):
    def setUp(self):
        MedicalImageResult.objects.create(
            file_name='test_file.dcm',
            result_data='test data'
        )

    def test_get_image_results(self):
        response = self.client.get(reverse('dicomresult-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)