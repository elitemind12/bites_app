from django.db import models
from django.urls import reverse


'''........ modal for storing bites categories ......''' 

class Categorie(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

'''........ modal for storing bites  ......''' 

class Menu(models.Model):
    category = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    image = models.ImageField(max_length=255,upload_to='images', default='default.jpg')

    def get_absolute_url(self):
       return reverse('bites:detail',kwargs={'pk':self.pk})
    
    def __str__(self):
        return self.name
