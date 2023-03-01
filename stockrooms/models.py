from django.db import models

class Store(models.Model):  
  code = models.CharField(primary_key=True, max_length=10, null=False, unique=True, verbose_name="Código SAP")
  name = models.CharField(max_length=100, null=False, unique=True, verbose_name="Descripción")

  class Meta:
    ordering = ["code"]

  def __str__(self):
    row = self.code + " | " + self.name
    return row


class Part(models.Model):
  sap_code = models.CharField(primary_key=True, max_length=25, null=False, unique=True, verbose_name="Código SAP")
  sup_code = models.CharField(max_length=20, null=False, unique=True, verbose_name="Código fabricante")
  description = models.CharField(max_length=120, null=False, verbose_name="Descripción repuesto")

  class Meta:
    ordering = ["sap_code"]

  def __str__(self):
    row = self.sap_code + " | " + self.sup_code + " | " + self.description
    return row

class Inventory(models.Model):
  part = models.ForeignKey(Part, null=True, blank=True, on_delete=models.CASCADE)
  store = models.ForeignKey(Store, null=True, blank=True, on_delete=models.CASCADE)
  qty = models.IntegerField(null=False, verbose_name='Cantidad')
  min = models.IntegerField(null=False, verbose_name='Minimo')
  order = models.IntegerField(null=False, verbose_name='Reorden')
  max = models.IntegerField(null=False, verbose_name='Maximo')

  class Meta:    
    constraints = [
      models.UniqueConstraint(fields=["part", "store"], name="unique_part")
    ]
    ordering = ["store", "part"]

  def __str__(self):
    row = self.part.sap_code +  " | " + self.store.code 
    return row
  