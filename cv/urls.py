from rest_framework.routers import DefaultRouter

from cv.views import CurriculumVitaeViewSet

router = DefaultRouter()
router.register('', CurriculumVitaeViewSet, basename='cv')
urlpatterns = router.urls
