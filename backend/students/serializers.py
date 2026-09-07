from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
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