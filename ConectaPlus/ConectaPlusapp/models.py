from django.db import models

# Create your models here.

class Perfil(models.Model):
    name    = models.CharField(max_length=50)
    idade   = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name


class Projeto(models.Model):
    name        = models.CharField(max_length= 100)
    descricao   = models.TextField(max_length= 500, blank = True, null= True)
    
    def __str__(self):
        return self.name
    
