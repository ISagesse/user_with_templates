from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=254)
    age = models.IntegerField()
