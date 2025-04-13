from django.db import models

class GalleryImage(models.Model):
    image = models.ImageField(upload_to='gallery/')
    category = models.CharField(max_length=100)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category
