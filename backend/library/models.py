from django.db import models
from students.models import Student


class LibraryCard(models.Model):
    student = models.OneToOneField(
        Student,
        on_delete=models.CASCADE,
        related_name='library_card'
    )
    card_number = models.CharField(max_length=20, unique=True)
    issue_date = models.DateField()
    expiry_date = models.DateField()

    def __str__(self):
        return self.card_number