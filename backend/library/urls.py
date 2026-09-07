from rest_framework.routers import DefaultRouter
from .views import LibraryCardViewSet


router = DefaultRouter()
router.register('', LibraryCardViewSet, basename='library-card')

urlpatterns = router.urls