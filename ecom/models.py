from django.db import models
from django.contrib.auth.models import User

class Cat(models.Model):
    cat_name = models.CharField(max_length = 25)
    def __str__(self):
        return self.cat_name


class Item(models.Model):
    name = models.TextField(max_length=250)
    price = models.IntegerField()
    description = models.TextField(max_length = 200)
    image_url = models.CharField(max_length=2033)
    user = models.ForeignKey(User, on_delete = models.SET_NULL, null=True)
    categorie = models.ForeignKey(Cat, on_delete = models.SET_NULL, null=True)
    def __str__(self):
        return self.name


class CartItem(models.Model):
    
    item = models.ForeignKey(Item, on_delete = models.CASCADE)
    quantity = models.IntegerField(default = 0)

    def __str__(self):
        return f'{self.item.name}'



