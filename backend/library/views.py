from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import LibraryCard
from .serializers import LibraryCardSerializer
from accounts.permissions import IsLibraryCardOwnerOrAdmin


class LibraryCardViewSet(ModelViewSet):
    serializer_class = LibraryCardSerializer
    permission_classes = [
        IsAuthenticated,
        IsLibraryCardOwnerOrAdmin
    ]

    def get_queryset(self):
        user = self.request.user

        # Admin → all library cards
        if (
            user.is_superuser
            or user.groups.filter(name='Admin').exists()
        ):
            return LibraryCard.objects.all()

        # Student → only their own card
        return LibraryCard.objects.filter(
            student__user=user
        )

    def create(self, request, *args, **kwargs):
        if not (
            request.user.is_superuser
            or request.user.groups.filter(name='Admin').exists()
        ):
            from rest_framework.response import Response
            from rest_framework import status

            return Response(
                {'detail': 'Only admins can create library cards.'},
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
                {'detail': 'Only admins can delete library cards.'},
                status=status.HTTP_403_FORBIDDEN
            )

        return super().destroy(request, *args, **kwargs)