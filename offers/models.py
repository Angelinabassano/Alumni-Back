from django.db import models
from django.conf import settings
from cloudinary.models import CloudinaryField


class Offer(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    logo = CloudinaryField('image', folder='offer_logos')
    company = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='offers')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

