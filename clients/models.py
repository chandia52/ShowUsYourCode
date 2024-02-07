from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Proyecto(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to="images/")
    