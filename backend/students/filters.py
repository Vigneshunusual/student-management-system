import django_filters
from .models import Student


class StudentFilter(django_filters.FilterSet):
    department_code = django_filters.CharFilter(
        field_name='department__code',
        lookup_expr='iexact'
    )
    class Meta:
        model = Student
        fields = [
            'department',
            'student_id',
            'enrollment_date',
            'department_code',
        ]