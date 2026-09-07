from django.db import models

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=20, unique=True)
    credits = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.code} - {self.name}"