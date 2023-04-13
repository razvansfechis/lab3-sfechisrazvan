from django.db import models

# Create your models here.

from django.db import models


class Pharmacy(models.Model):
    nr_employees = models.IntegerField()
    security = models.BooleanField()
    nr_customers = models.IntegerField()
    pharmacy_name = models.CharField(max_length=50)
    director = models.CharField(max_length=50)


class Customer(models.Model):
    sex_options = [
        ["M", "Male"],
        ["F", "Female"]
    ]
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    sex = models.CharField(choices=sex_options, max_length=20)
    pharmacy = models.ForeignKey(Pharmacy, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.id) + ' ' + self.first_name + ' ' + self.last_name
    

class ProductDelivery(models.Model):
    delivery_person = models.CharField(blank=True, max_length=100)
    fee = models.IntegerField(blank=True, default=0)
    date = models.DateField()
    pickup = models.BooleanField()
    details = models.TextField(blank=True, max_length=300)
    pharmacy = models.ForeignKey(Pharmacy, on_delete=models.DO_NOTHING)
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.id) + ' ' + str(self.pharmacy) + ' ' + str(self.customer)