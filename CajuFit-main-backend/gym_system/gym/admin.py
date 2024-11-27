from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Exercicio, Treino, TreinoExercicio, Aluno, Progresso

admin.site.register(Exercicio)
admin.site.register(Treino)
admin.site.register(TreinoExercicio)
admin.site.register(Aluno)
admin.site.register(Progresso)
