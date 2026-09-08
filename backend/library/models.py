from django.db import models
from students.models import Student
from django.core.exceptions import ValidationError


class LibraryCard(models.Model):
    student = models.OneToOneField(
        Student,
        on_delete=models.CASCADE,
        related_name='library_card'
    )
    card_number = models.CharField(max_length=20, unique=True)
    issue_date = models.DateField()
    expiry_date = models.DateField()

    def clean(self):  #clean() is useful when validation depends on multiple fields. so, The expiry date cannot be before the issue date.
        if self.expiry_date < self.issue_date:
            raise ValidationError(
                'Expiry date cannot be before issue date.'
            )

    def __str__(self):
        return self.card_number