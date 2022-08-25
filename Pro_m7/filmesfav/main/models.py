from django.db import models

class ProjetoDjango(models.Model):
    #Colunas de filmes
    Filme = models.CharField(max_length=50)
    Descricao = models.TextField()
    Gênero = models.CharField(max_length=50)    
    Idade = models.CharField(max_length=10)

    def __str__(self):
        return self.Filme