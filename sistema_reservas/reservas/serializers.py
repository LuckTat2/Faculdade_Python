from rest_framework import serializers
from .models import User, Professor, Laboratorio, Reserva

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__'

class LaboratorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Laboratorio
        fields = '__all__'

class ReservaSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    professor = ProfessorSerializer(read_only=True)
    laboratorio = LaboratorioSerializer(read_only=True)

    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='user', write_only=True)
    professor_id = serializers.PrimaryKeyRelatedField(queryset=Professor.objects.all(), source='professor', write_only=True)
    laboratorio_id = serializers.PrimaryKeyRelatedField(queryset=Laboratorio.objects.all(), source='laboratorio', write_only=True)

    class Meta:
        model = Reserva
        fields = ['id', 'data_reserva', 'hora_inicio', 'hora_fim', 'user', 'professor', 'laboratorio', 'user_id', 'professor_id', 'laboratorio_id']