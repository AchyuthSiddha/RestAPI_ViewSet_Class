from django.db import models

# Create your models here.


class Product_category(models.Model):
    PCID=models.PositiveIntegerField()
    PCname=models.CharField(max_length=100)
    
    def __str__(self):
        return self.PCname
    


class Product(models.Model):
    PID=models.IntegerField()
    PCname=models.ForeignKey(Product_category,on_delete=models.CASCADE)
    pname=models.CharField(max_length=100)
    Price=models.DecimalField(max_digits=8,decimal_places=2)
    Pdate=models.DateField()
    
    def __str__(self):
        return self.pname
    
    