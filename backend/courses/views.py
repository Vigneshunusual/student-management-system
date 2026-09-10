from rest_framework.viewsets import ModelViewSet
from .models import Course
from .serializers import CourseSerializer
from accounts.permissions import IsAdminOrReadOnly


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all().order_by('id')
    serializer_class = CourseSerializer
    permission_classes = [IsAdminOrReadOnly]
    filterset_fields = ['credits', 'code', 'name']
    search_fields = ['name', 'code']