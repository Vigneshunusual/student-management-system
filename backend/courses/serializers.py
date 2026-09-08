from rest_framework import serializers
from .models import Course


class CourseSerializer(serializers.ModelSerializer):
    credits=serializers.IntegerField(min_value=1, max_value=5)
    class Meta:
        model = Course
        fields = ['id', 'name', 'code', 'credits']