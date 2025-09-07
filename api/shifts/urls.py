from rest_framework.routers import DefaultRouter

from api.pickup_points.views import PickupPointViewSet

router = DefaultRouter()
router.register('work-shifts', PickupPointViewSet, basename='work-shift')

urlpatterns = router.urls