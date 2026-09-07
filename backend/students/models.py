from django.db import models
from django.contrib.auth.models import User
from departments.models import Department
from courses.models import Course


class Student(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='student_profile'
    )
    student_id = models.CharField(max_length=20, unique=True)
    department = models.ForeignKey(
        Department,
        on_delete=models.PROTECT,
        related_name='students'
    )
    courses = models.ManyToManyField(
        Course,
        related_name='students',
        blank=True
    )
    date_of_birth = models.DateField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    enrollment_date = models.DateField()

    def __str__(self):
        return self.student_id


    