from django.db import models

# Create your models here.

class PlanA(models.Model):
    uc = models.CharField(max_length=100)
    evento = models.CharField(max_length=20)
    ch = models.IntegerField()
    obj = models.TextField(max_length=1000)
    docente = models.CharField(max_length=150)
    
    def __str__(self):
        return self.uc