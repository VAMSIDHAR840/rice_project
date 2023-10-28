from django.db import models
import datetime
from django.db import models

# Create your models here.
class categories(models.Model):
    categories_id = models.PositiveIntegerField(primary_key=True, max_length=10)
    name = models.CharField(max_length=100)
    modified_date = models.DateField(default=datetime.date.today())

class brand(models.Model):
    brand_id = models.PositiveIntegerField(primary_key=True, max_length=10)
    categories_id = models.ForeignKey(categories, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    price =models.PositiveIntegerField()
    modified_date = models.DateField(default=datetime.date.today())

class user(models.Model):
    user_id = models.PositiveIntegerField(primary_key=True, max_length=10)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    user_type = models.CharField(max_length=10)
    modified_date = models.DateField(default=datetime.date.today())
    address = models.CharField(max_length=150)
    mobile = models.PositiveIntegerField(max_length=10)

class order(models.Model):
    order_id = models.PositiveIntegerField(primary_key=True, max_length=10)
    user_id = models.ForeignKey(user, on_delete=models.CASCADE)
    categories_id = models.ForeignKey(categories, on_delete=models.CASCADE)
    brand_id = models.ForeignKey(brand, on_delete=models.CASCADE)
    order_quantity = models.PositiveIntegerField(max_length=10)
    total_price = models.PositiveIntegerField()
    order_status = models.CharField(max_length=10)
    modified_date = models.DateField(default=datetime.date.today())

class purchase(models.Model):
    purchase_id = models.PositiveIntegerField(primary_key=True, max_length=100)
    user_id = models.ForeignKey(user, on_delete=models.CASCADE)
    categories_id = models.ForeignKey(categories, on_delete=models.CASCADE)
    brand_id = models.ForeignKey(brand, on_delete=models.CASCADE)
    order_quantity = models.ForeignKey(order, on_delete=models.CASCADE)
    total_price = models.PositiveIntegerField()
    status = models.CharField(max_length=10)
    modified_date = models.DateField(default=datetime.date.today())

class payment(models.Model):
    payment_id = models.CharField(primary_key=True, max_length=100)
    order_id = models.ForeignKey(order, on_delete=models.CASCADE)
    purchase_id = models.ForeignKey(purchase, on_delete=models.CASCADE)
    modified_date = models.DateField(default=datetime.date.today())
    amount_paid = models.PositiveSmallIntegerField()
    next_date = models.DateField()
    status = models.CharField(max_length=10)

class tracking(models.Model):
    tracking_id = models.PositiveIntegerField(primary_key=True, max_length=100)
    order_id = models.ForeignKey(order, on_delete=models.CASCADE)
    categories_id = models.ForeignKey(categories, on_delete=models.CASCADE)
    status = models.CharField(max_length=10)
    modified_date = models.DateField(default=datetime.date.today())

class reminder(models.Model):
    reminder_id = models.PositiveIntegerField(max_length=100)
    reminder_type = models.CharField(max_length=10)
    comment = models.TextField(max_length=250)

    