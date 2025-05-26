from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ProfessorViewSet, LaboratorioViewSet, ReservaViewSet

router = DefaultRouter()
router.register(r'usuarios', UserViewSet)
router.register(r'professores', ProfessorViewSet)
router.register(r'laboratorios', LaboratorioViewSet)
router.register(r'reservas', ReservaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]