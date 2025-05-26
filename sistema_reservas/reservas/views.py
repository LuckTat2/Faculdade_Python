from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import User, Professor, Laboratorio, Reserva
from .serializers import UserSerializer, ProfessorSerializer, LaboratorioSerializer, ReservaSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer

    @action(detail=True, methods=['get'])
    def reservas(self, request, pk=None):
        professor = self.get_object()
        reservas = professor.reservas.all()
        serializer = ReservaSerializer(reservas, many=True)
        return Response(serializer.data)

class LaboratorioViewSet(viewsets.ModelViewSet):
    queryset = Laboratorio.objects.all()
    serializer_class = LaboratorioSerializer

    @action(detail=True, methods=['get'])
    def reservas(self, request, pk=None):
        laboratorio = self.get_object()
        reservas = laboratorio.reservas.all()
        serializer = ReservaSerializer(reservas, many=True)
        return Response(serializer.data)

class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
