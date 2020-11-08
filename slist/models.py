from django.db import models

# Create your models here.


class Category(models.Model):
    category = models.CharField(max_length=15)

    def __str__(self):
        return self.category
    class Meta():
        verbose_name_plural = 'Categories'


class Supermarket(models.Model):
    supermarket = models.CharField(max_length=30)
    products = models.ManyToManyField('Product', through='ProductBySupermarket')
    def __str__(self):
        return self.supermarket


class Brand(models.Model):
    brand = models.CharField(max_length=30)
    Supermarket = models.ForeignKey(
        Supermarket, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.brand


class Product(models.Model):
    product = models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.product


class ProductBySupermarket(models.Model):
    price = models.IntegerField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True)
    supermarket = models.ForeignKey(
        Supermarket, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"${str(self.price)} | {self.product} | {self.supermarket} | {self.brand}"
