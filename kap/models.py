from django.db import models

# Create your models here.

class DairyProduct(models.Model):
    name = models.CharField(max_length=100)
    photo = models.FileField(blank=True)
    desc = models.TextField(max_length=500, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
        return self.photo
        return self.desc
        return self.price
        return self.stock


class Amul_1_Ltr_Ice_Cream_Tubs(models.Model):
    name = models.CharField(max_length=100)
    photo = models.FileField(blank=True)
    desc = models.TextField(max_length=500, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
        return self.photo
        return self.desc
        return self.price
        return self.stock

class Amul_2_Ltr_Ice_Cream_Bricks(models.Model):
        name = models.CharField(max_length=100)
        photo = models.FileField(blank=True)
        desc = models.TextField(max_length=500, blank=True)
        price = models.DecimalField(max_digits=10, decimal_places=2)
        stock = models.BooleanField(default=True)
        created = models.DateTimeField(auto_now_add=True)
        updated = models.DateTimeField(auto_now=True)

        def __str__(self):
            return self.name
            return self.photo
            return self.desc
            return self.price
            return self.stock

class Amul_750ml_Ice_Cream_Bricks(models.Model):
        name = models.CharField(max_length=100)
        photo = models.FileField(blank=True)
        desc = models.TextField(max_length=500, blank=True)
        price = models.DecimalField(max_digits=10, decimal_places=2)
        stock = models.BooleanField(default=True)
        created = models.DateTimeField(auto_now_add=True)
        updated = models.DateTimeField(auto_now=True)

        def __str__(self):
            return self.name
            return self.photo
            return self.desc
            return self.price
            return self.stock
