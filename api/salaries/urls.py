from rest_framework.routers import DefaultRouter

from api.salaries.views import SalaryViewSet

router = DefaultRouter()
router.register('salaries', SalaryViewSet, basename='salary')

urlpatterns = router.urls