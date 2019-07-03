from django.db import models
from django.contrib.auth.models import User

class Items(models.Model):
    vendorName = models.TextField()
    itemName = models.TextField()
    catNo = models.TextField(primary_key=True)
    price = models.TextField()
    quantity = models.TextField()
    description = models.CharField(max_length=255)
    
    def __str__(self):
    	return self.itemName