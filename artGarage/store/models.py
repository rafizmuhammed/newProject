from django.db import models

# Create your models here.

class categories(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pic')
    price =models.IntegerField()
    date =models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name    