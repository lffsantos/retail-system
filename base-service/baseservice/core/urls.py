from rest_framework.routers import DefaultRouter

from baseservice.core.views import UserViewSet, ProductViewSet

app_name = 'core'


router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'products', ProductViewSet, basename='product')
urlpatterns = router.urls
