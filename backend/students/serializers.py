from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    student_id=serializers.RegexField(regex=r'^STU\d{3,}$',
                error_messages={'invalid': 'Student ID must start with "STU" followed by at least three digits.'})
    class Meta:
        model = Student
        fields = [
            'id',
            'user',
            'student_id',
            'department',
            'courses',
            'date_of_birth',
            'phone',
            'address',
            'enrollment_date',
        ]