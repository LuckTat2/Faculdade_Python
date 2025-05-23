from rest_framework import serializers
from .models import Materia

class MateriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materia
        fields = "__all__" # Pega todos os campos do modelo