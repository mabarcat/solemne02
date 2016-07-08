from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True,null=True)
    banner = models.ImageField(upload_to='images/banner_categories',blank=True,null=True)
    status = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    sku = models.CharField(max_length=100,unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    price = models.DecimalField(max_digits=11, decimal_places=2)
    trademark = models.CharField(max_length=100)
    category = models.ForeignKey(Category)
    image = models.ImageField(upload_to='images/data',blank=True,null=True)
    status = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Trademark(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/data',blank=True,null=True)
    category = models.ForeignKey(Category)
    status = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name