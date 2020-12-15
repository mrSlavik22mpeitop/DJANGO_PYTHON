from django.db import models

# Create your models here.
class Payment(models.Model):
    customers_id = models.ForeignKey('customers.Customer', on_delete=models.CASCADE)
    products_id = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    payment_Date = models.DateField(max_length=50)
    amount = models.CharField(max_length=50)

