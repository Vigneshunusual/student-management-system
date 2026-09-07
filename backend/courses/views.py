from rest_framework.viewsets import ModelViewSet

from .models import Course
from .serializers import CourseSerializer
from accounts.permissions import IsAdminOrReadOnly


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAdminOrReadOnly]