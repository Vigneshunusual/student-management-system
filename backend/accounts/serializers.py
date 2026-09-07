from django.contrib.auth.models import User
from django.db import transaction
from rest_framework import serializers

from departments.models import Department
from students.models import Student

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    student_id = serializers.CharField()
    department = serializers.PrimaryKeyRelatedField(
        queryset=Department.objects.all()
    )
    date_of_birth = serializers.DateField()
    phone = serializers.CharField()
    address = serializers.CharField()
    enrollment_date = serializers.DateField()

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'student_id',
            'department',
            'date_of_birth',
            'phone',
            'address',
            'enrollment_date',
        ]

    @transaction.atomic
    def create(self, validated_data):
        student_data = {
            'student_id': validated_data.pop('student_id'),
            'department': validated_data.pop('department'),
            'date_of_birth': validated_data.pop('date_of_birth'),
            'phone': validated_data.pop('phone'),
            'address': validated_data.pop('address'),
            'enrollment_date': validated_data.pop('enrollment_date'),
        }

        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )

        Student.objects.create(
            user=user,
            **student_data
        )

        return user


#@transaction.atomic
#means the User and Student creation happen as one database transaction.
#If Student creation fails, Django rolls back the User creation too.



