from django.db import models
from django.contrib.auth.models import User


class Aluno(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, editable=False)
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    peso = models.FloatField()
    altura = models.FloatField()
    plano = models.CharField(max_length=50, choices=[('mensal', 'Mensal'), ('anual', 'Anual')])
    data_cadastro = models.DateField(auto_now_add=True)
    matricula_inicio = models.DateField(null=True, blank=True)
    matricula_vencimento = models.DateField(null=True, blank=True)
    tipo_usuario = models.CharField(max_length=20, choices=[('aluno', 'Aluno'), ('professor', 'Professor')], default='aluno')

    def __str__(self):
        return self.nome


class Exercicio(models.Model):
    nome = models.CharField(max_length=100)
    grupo_muscular = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Treino(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name='treinos')
    descricao = models.TextField()
    data = models.DateField()

    def __str__(self):
        return f"Treino de {self.aluno.nome} - {self.data}"


class TreinoExercicio(models.Model):
    treino = models.ForeignKey(Treino, on_delete=models.CASCADE, related_name='exercicios')
    exercicio = models.ForeignKey(Exercicio, on_delete=models.CASCADE)
    carga = models.FloatField(default=0.0)
    series = models.IntegerField(default=3)
    repeticoes = models.IntegerField(default=12)
    concluido = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.exercicio.nome} - {self.treino.aluno.nome}"


class Progresso(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name='progresso')
    data = models.DateField(auto_now_add=True)
    peso = models.FloatField()

    def __str__(self):
        return f"Progresso de {self.aluno.nome} - {self.data}"
