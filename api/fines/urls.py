from rest_framework.routers import DefaultRouter

from api.fines.views import FineViewSet

router = DefaultRouter()
router.register('fines', FineViewSet, basename='fine')

urlpatterns = router.urls