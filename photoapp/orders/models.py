from django.db import models
# Create your models here.
class Order(models.Model):
    customers_id = models.ForeignKey('customers.Customer', on_delete=models.CASCADE)
    order_date = models.DateField(max_length=50)
    required_date = models.DateField(max_length=50)
    shipped_date = models.DateField(max_length=50)
    status = models.CharField(max_length=50)



class Meta:
    db_table = 'order'

    def __str__(self):
        return self.first_name