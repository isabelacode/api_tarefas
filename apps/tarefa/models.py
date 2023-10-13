from django.db import models

class Tarefas(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_conclusao = models.DateTimeField(null=True, blank=True)
    concluida = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo