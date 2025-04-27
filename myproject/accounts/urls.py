from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, register_page, login_page, home_page

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', register_page, name='register'),
    path('Login/', login_page, name='login'),
    path('Home/', home_page, name='home'),
]