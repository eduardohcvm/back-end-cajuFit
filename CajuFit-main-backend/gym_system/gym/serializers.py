from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Aluno, Exercicio, Treino, TreinoExercicio, Progresso

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = '__all__'

class ExercicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercicio
        fields = '__all__'

class TreinoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Treino
        fields = '__all__'

class TreinoExercicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = TreinoExercicio
        fields = '__all__'

class ProgressoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Progresso
        fields = '__all__'

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user
