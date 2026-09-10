from rest_framework.viewsets import ModelViewSet

from .models import Department
from .serializers import DepartmentSerializer
from accounts.permissions import IsAdminOrReadOnly


class DepartmentViewSet(ModelViewSet):
    queryset = Department.objects.all().order_by('id')
    serializer_class = DepartmentSerializer
    permission_classes = [IsAdminOrReadOnly]    