from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=20, decimal_places=10)
    expiry_date = models.DateField()
    manufacturing_date = models.DateField()
