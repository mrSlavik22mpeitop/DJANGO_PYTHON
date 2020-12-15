from django.db import models
#DataFlair Models
class Product(models.Model):
    product_name = models.CharField(max_length = 50)
    product_company = models.CharField(max_length = 50)
    price = models.CharField(max_length = 40)
    rating = models.CharField(max_length = 50)

    def __str__(self):
        return self.product_name

