from django.contrib.auth.models import AbstractUser
from django.db import models
from cloudinary.models import CloudinaryField


class User(AbstractUser):
    ROLE_CHOICES = (
        ('rp', 'RP'),
        ('coder', 'Coder'),
        ('empresa', 'Empresa'),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    profile_picture = CloudinaryField('image', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    company_name = models.CharField(max_length=100, blank=True, null=True)
    nif = models.CharField(max_length=20, unique=True, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    rp = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='coder_rp')
    school = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.username
