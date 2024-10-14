from django.db import models


class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Coder(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    front_end_skills = models.ManyToManyField(Skill, related_name='front_end_coders')
    back_end_skills = models.ManyToManyField(Skill, related_name='back_end_coders')
    experience = models.CharField(max_length=50)
    availability = models.CharField(max_length=50)
    language = models.CharField(max_length=50)

    def __str__(self):
        return self.name



