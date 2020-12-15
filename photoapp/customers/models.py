from django.db import models
#DataFlair Models
class Customer(models.Model):
    employees_id = models.ForeignKey('employees.Employee', on_delete=models.CASCADE)
    products_id = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    first_name = models.CharField(max_length = 50)
    second_name = models.CharField(max_length = 50)
    email = models.EmailField(blank = True)
    phone = models.CharField(max_length = 15)
    location = models.CharField(max_length = 50)
    postal_Code = models.CharField(max_length = 40)

    def __str__(self):
        return self.first_name

