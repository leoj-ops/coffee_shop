from django.db import models

# Create your models here.
from django.db import models

class Profile(models.Model):
    customer_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50)
    email_id = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    loyalty_point = models.IntegerField(default=0, null=True,blank=True)


class Transaction(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    item = models.CharField(max_length=255)
    price_paid = models.DecimalField(max_digits=10, decimal_places=2)