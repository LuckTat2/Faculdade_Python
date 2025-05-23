from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MateriaViewSet

router = DefaultRouter()
# Cria automaticamente GET, POST, PUT, DELETE
router.register(r'materias', MateriaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]