from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import Student
from .serializers import StudentSerializer
from accounts.permissions import IsOwnerOrAdmin
from django_filters.rest_framework import DjangoFilterBackend
from .filters import StudentFilter

class StudentViewSet(ModelViewSet):
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]
    # filterset_fields = ['department', 'student_id','enrollment_date']
    filter_backends = [DjangoFilterBackend]
    filterset_class = StudentFilter

    def get_queryset(self):
        user = self.request.user

        # Admin → see all students
        if (
            user.is_superuser
            or user.groups.filter(name='Admin').exists()
        ):
            return Student.objects.all()

        # Student → see only their own record
        return Student.objects.filter(user=user)

    def create(self, request, *args, **kwargs):
        if not (
            request.user.is_superuser
            or request.user.groups.filter(name='Admin').exists()
        ):
            from rest_framework.response import Response
            from rest_framework import status

            return Response(
                {'detail': 'Only admins can create students.'},
                status=status.HTTP_403_FORBIDDEN
            )

        return super().create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        if not (
            request.user.is_superuser
            or request.user.groups.filter(name='Admin').exists()
        ):
            from rest_framework.response import Response
            from rest_framework import status

            return Response(
                {'detail': 'Only admins can delete students.'},
                status=status.HTTP_403_FORBIDDEN
            )

        return super().destroy(request, *args, **kwargs)