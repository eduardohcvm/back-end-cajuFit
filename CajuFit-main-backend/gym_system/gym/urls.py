from django.urls import path, include
from .views import RegisterView, LoginView
from .views import UsuarioView
from rest_framework.routers import DefaultRouter
from .views import (
    AlunoViewSet,
    ExercicioViewSet,
    TreinoViewSet,
    TreinoExercicioViewSet,
    ProgressoViewSet,
    UserInfoView,
    TreinoInfoView
)

router = DefaultRouter()
router.register(r'alunos', AlunoViewSet)
router.register(r'exercicios', ExercicioViewSet)
router.register(r'treinos', TreinoViewSet)
router.register(r'treino-exercicios', TreinoExercicioViewSet)
router.register(r'progresso', ProgressoViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('api/usuarios/', UsuarioView.as_view(), name='usuarios'),
    path('api/user-info/', UserInfoView.as_view(), name='user-info'),
    path('api/treinos/', TreinoInfoView.as_view(), name='treino-info'),
]
