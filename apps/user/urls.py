from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router = DefaultRouter()
router.register(
    prefix="user",
    viewset=UsersApiView
)

router.register(
    prefix='avatar',
    viewset=UsersAvatarApiView
)


urlpatterns = router.urls
