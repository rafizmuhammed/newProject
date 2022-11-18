from django.db import models

# Create your models here.

class categories(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pic')
    price =models.IntegerField()
    date =models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name 


class collections(models.Model):   
    elements = models.ForeignKey(categories,related_name ='element',on_delete =models.CASCADE)
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pic')
    desc = models.TextField()
    price = models.IntegerField() 
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name