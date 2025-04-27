from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet  # ou TaskList si tu utilises APIView

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)  # Utilisé avec ViewSet

urlpatterns = [
    path('', include(router.urls)),  # Pour ViewSet
    # Ou, pour APIView :
    # path('tasks/', TaskList.as_view(), name='task-list'),
]