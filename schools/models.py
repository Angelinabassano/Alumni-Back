from django.db import models

class School(models.Model):
    name = models.CharField(max_length=100)
    objects = models.Manager()
    def __str__(self):
        return self.name
