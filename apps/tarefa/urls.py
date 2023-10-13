from django.urls import include, path
from rest_framework import routers

from .views import TarefasViewSet

app_name = 'tarefas'

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'tarefas', TarefasViewSet, basename='tarefas')

urlpatterns = [
    path(r'', include(router.urls)),
]
