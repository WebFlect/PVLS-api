from rest_framework.routers import DefaultRouter

from api.trainings.views import TrainingViewSet

router = DefaultRouter()
router.register('trainings', TrainingViewSet, basename='training')

urlpatterns = router.urls