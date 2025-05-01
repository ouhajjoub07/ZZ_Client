from django.urls import path
from ZAppUser.api.viewset import ProductViewSet
from rest_framework.routers import DefaultRouter, SimpleRouter

"""
default router est utilise pour les operations CRUD
par Contre simple router est utilise pour les seules operations de lecture
"""

router = DefaultRouter()
router.register('v1/product', ProductViewSet, basename='product')

urlpatterns = router.urls