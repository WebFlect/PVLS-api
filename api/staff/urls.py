from rest_framework.routers import DefaultRouter

from api.staff.views import UserViewSet

router = DefaultRouter()
router.register('staffs', UserViewSet, basename='staff')

urlpatterns = router.urls