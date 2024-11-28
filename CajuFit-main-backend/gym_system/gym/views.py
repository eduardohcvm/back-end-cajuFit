from rest_framework import viewsets
from django.shortcuts import render
from .models import Aluno, Exercicio, Treino, TreinoExercicio, Progresso
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from .serializers import (
    AlunoSerializer,
    ExercicioSerializer,
    TreinoSerializer,
    TreinoExercicioSerializer,
    ProgressoSerializer,
)

class TreinoInfoView(APIView):
    permission_classes = [IsAuthenticated]  # Garantir que apenas usuários autenticados acessem

    def get(self, request):
        treino = Treino.objects.all()
        serializer = TreinoSerializer(treino, many=True)
        return Response(serializer.data)

class TreinoExercicioInfoView(APIView):
    permission_classes = [IsAuthenticated]  # Garantir que apenas usuários autenticados acessem

    def get(self, request):
        treinoexercicio = TreinoExercicio.objects.all()
        serializer = TreinoExercicioSerializer(treinoexercicio, many=True)
        return Response(serializer.data)

class UserInfoView(APIView):
    permission_classes = [IsAuthenticated]  # Garantir que apenas usuários autenticados acessem

    def get(self, request):
        user = request.user
        return Response({
            "username": user.username,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
        })



class UsuarioView(APIView):
    permission_classes = [AllowAny]  # Permitir acesso sem autenticação

    def get(self, request):
        user = request.user if request.user.is_authenticated else None
        return Response({
            'username': user.username if user else 'Guest',
            'email': user.email if user else '',
            'first_name': user.first_name if user else '',
            'last_name': user.last_name if user else '',
        })

    def post(self, request):
        # Adicionar a lógica para criar um novo usuário
        data = request.data
        return Response({"message": "POST request received", "data": data}, status=status.HTTP_201_CREATED)


class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    permission_classes = [AllowAny]


class ExercicioViewSet(viewsets.ModelViewSet):
    queryset = Exercicio.objects.all()
    serializer_class = ExercicioSerializer
    permission_classes = [AllowAny]


class TreinoViewSet(viewsets.ModelViewSet):
    queryset = Treino.objects.all()
    serializer_class = TreinoSerializer
    permission_classes = [AllowAny]


class TreinoExercicioViewSet(viewsets.ModelViewSet):
    queryset = TreinoExercicio.objects.all()
    serializer_class = TreinoExercicioSerializer
    permission_classes = [AllowAny]


class ProgressoViewSet(viewsets.ModelViewSet):
    queryset = Progresso.objects.all()
    serializer_class = ProgressoSerializer
    permission_classes = [AllowAny]


def lista_alunos(request):
    alunos = Aluno.objects.all()
    return render(request, 'lista_alunos.html', {'alunos': alunos})


def detalhes_aluno(request, aluno_id):
    aluno = Aluno.objects.get(id=aluno_id)
    return render(request, 'detalhes_aluno.html', {'aluno': aluno})


class RegisterView(APIView):
    permission_classes = [AllowAny]  # Permissão pública

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'message': 'Usuário registrado com sucesso!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(ObtainAuthToken):
    permission_classes = [AllowAny]  # Permissão pública

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.id,
            'username': user.username
        })