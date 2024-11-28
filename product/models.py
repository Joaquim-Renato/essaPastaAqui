from django.db import models

class Product(models.Model):
    codprod = models.AutoField(primary_key=True)
    nameprod = models.CharField(max_length= 100)
    categoryprod =  models.CharField(max_length= 100)
    descprod = models.TextField()
    brandprod = models.CharField(max_length = 50)
    manudateprod = models.DateField()
    weightprod = models.DecimalField(max_digits = 6, decimal_places = 2)
    
class  PriceProd(models.Model):
    codprice = models.AutoField(primary_key=True)
    codprod = models.ForeignKey(Product, on_delete=models.CASCADE, related_name= 'codigo')
    priceprod = models.DecimalField(max_digits= 8, decimal_places= 2)
    dateverify = models.DateField()
 