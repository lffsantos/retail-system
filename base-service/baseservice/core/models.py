from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    birth_date = models.DateField(null=False, blank=False)

    class Meta:
        ordering = ('first_name',)
        managed = False
        db_table = 'users'

    def __str__(self):
        return self.first_name


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, null=False, blank=False)
    description = models.CharField(max_length=200, null=False, blank=False)
    price = models.DecimalField(max_digits=17, decimal_places=2)
    base_discount_percent = models.FloatField(default=0)
    
    class Meta:
        ordering = ('id',)
        managed = False
        db_table = 'products'

    def __str__(self):
        return self.title
