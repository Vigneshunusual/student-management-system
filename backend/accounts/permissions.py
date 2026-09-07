from rest_framework.permissions import BasePermission
from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsStudent(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.groups.filter(name='Student').exists()
        )


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.groups.filter(name='Admin').exists()
        )

class IsOwnerOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.groups.filter(name='Admin').exists():
            return True

        return obj.user == request.user

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        if request.method in SAFE_METHODS:
            return True

        return (
            request.user.is_superuser
            or request.user.groups.filter(name='Admin').exists()
        )

class IsLibraryCardOwnerOrAdmin(BasePermission):

    def has_object_permission(self, request, view, obj):
        if (
            request.user.is_superuser
            or request.user.groups.filter(name='Admin').exists()
        ):
            return True

        return obj.student.user == request.user