from django.db import models

class storedb(models.Model):
    product = models.CharField(max_length=50,primary_key=True)
    Category = models.CharField(max_length=50)
    price = models.IntegerField()
    images = models.ImageField(upload_to="files")
