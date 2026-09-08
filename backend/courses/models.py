from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=20, unique=True)
    credits = models.PositiveIntegerField(
        validators=[MinValueValidator(1),MaxValueValidator(5)]
    )

    def __str__(self):
        return f"{self.code} - {self.name}"