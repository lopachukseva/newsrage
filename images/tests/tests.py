from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase

from images.models import Image


class ImageModelTest(TestCase):
    def test_image_model_save_and_retrieve(self):
        image = Image()
        image_path = "images/tests/test_image.jpeg"
        image.title = "Test"
        image.photo = SimpleUploadedFile(
            name='test_image.jpg',
            content=open(image_path, 'rb').read(),
            content_type='image/jpeg')
        image.save()

        self.assertEqual(Image.objects.count(), 1)
