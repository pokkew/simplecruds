from django.db import models

# Create your models here.
class Item_plan(models.Model):
    plana = models.ForeignKey('PlanA',on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    proced = models.TextField(max_length=1000)
    recursos = models.CharField(max_length=100)
    
    def __str(self):
        return self.content