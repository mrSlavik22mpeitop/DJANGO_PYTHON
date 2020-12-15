from django.db import models
#DataFlair Models
class Employee(models.Model):
    first_name = models.CharField(max_length = 50)
    second_name = models.CharField(max_length = 50)
    email = models.EmailField(blank = True)
    phone = models.CharField(max_length = 15)
    office_code = models.CharField(max_length=40)
    position = models.CharField(max_length=70)


    def __str__(self):
        return self.first_name