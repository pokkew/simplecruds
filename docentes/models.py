from django.db import models

# Create your models here.

class Docente(models.Model):
    nome = models.CharField(max_length=100)
    dataCad = models.DateTimeField(auto_now = True)
    dataMod = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.nome
