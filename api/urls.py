from rest_framework.routers import DefaultRouter

from api.views import CurriculumVitaeViewSet

router = DefaultRouter()
router.register('', CurriculumVitaeViewSet, basename='api')
urlpatterns = router.urls
