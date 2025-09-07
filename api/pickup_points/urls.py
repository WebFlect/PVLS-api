from rest_framework.routers import DefaultRouter

from api.pickup_points.views import PickupPointViewSet

router = DefaultRouter()
router.register('pickup-points', PickupPointViewSet, basename='pickup-point')

urlpatterns = router.urls