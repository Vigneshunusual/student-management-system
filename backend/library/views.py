from rest_framework.viewsets import ModelViewSet
from .models import LibraryCard
from .serializers import LibraryCardSerializer


class LibraryCardViewSet(ModelViewSet):
    queryset = LibraryCard.objects.all()
    serializer_class = LibraryCardSerializer