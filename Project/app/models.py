from django.db import models

# Create your models here.
class Cards(models.Model):
    name=models.CharField(max_length=30)
    rate=models.IntegerField()
    image=models.ImageField(upload_to='shoes')