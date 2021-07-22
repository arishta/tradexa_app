from django.db import models

class Product(models.Model):
    name = models.CharField(max_length = 255)
    weight = models.DecimalField(max_digits = 4, decimal_places = 2)
    created_at = models.DateTimeField(blank = True, null = True, auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    price = models.DecimalField(max_digits = 6, decimal_places = 2)

    def __str__(self):
        return self.name

    class Meta: 
        db_table = "product"