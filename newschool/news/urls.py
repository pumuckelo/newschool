from rest_framework import routers
from .api import PostViewSet

router = routers.DefaultRouter()
router.register('api/news', PostViewSet, 'news')

urlpatterns = router.urls