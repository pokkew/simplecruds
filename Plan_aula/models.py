from django.db import models
from docentes.models import Docente


# Create your models here.



class PlanA(models.Model):
    uc = models.CharField(max_length=100)
    evento = models.CharField(max_length=20)
    ch = models.IntegerField()
    obj = models.TextField(max_length=1000)
    docente = models.ForeignKey(Docente,on_delete=models.CASCADE)

    
    def __str__(self):
        return self.uc

