from django.db import models

# Create your models here.
class User(models.Model):
    name = model.CharField(max_length=200)
    
    class meta:
        pass
