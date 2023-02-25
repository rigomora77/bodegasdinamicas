from django.db import models

class Store(models.Model):  
  code = models.IntegerField(primary_key=True, null=False, unique=True, verbose_name="Código SAP")
  name = models.CharField(max_length=100, null=False, unique=True, verbose_name="Descripción")
