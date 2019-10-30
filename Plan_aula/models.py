from django.db import models
from docentes.models import Docente
from django.conf import settings
from django.contrib.auth import get_user_model

# Create your models here.


def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]


class PlanA(models.Model):
    uc = models.CharField(max_length=100)
    evento = models.CharField(max_length=20)
    ch = models.IntegerField()
    obj = models.TextField(max_length=1000)
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET(get_sentinel_user), default=1)

    
    def __str__(self):
        return self.uc

