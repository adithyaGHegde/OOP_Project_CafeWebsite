from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.base import Model

ST_CHOICES = (
    ('Andhra Pradesh','Andhra Pradesh'),
    ('Delhi','Delhi'),
    ('Goa','Goa'),
    ('Karnataka','Karnataka'),
    ('kerala','kerala'),
    ('Madhya Pradesh','Madhya Pradesh'),
    ('Maharastra','Maharastra'),
    ('Tamil Nadu','Tamil Nadu'),
    ('Telangana','Telangana'),
    ('West Bengal','West Bengal'),
)
class customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    state = models.CharField(choices=ST_CHOICES, max_length=50)

def __str__(self):
    return str(self.id)


CATEGORY_CHOICES = (
    ('C', 'COFFEE'),
    ('T', 'TEA'),
    ('S', 'SNACKS'),
    ('B', 'BRUNCH'),
    
)
class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    brand = models.CharField(max_length=100)
    category = models.CharField( choices=CATEGORY_CHOICES, max_length=2)
    product_image = models.ImageField(upload_to='producting')


def __str__(self):
    return str(self.id)

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

def __str__(self):
    return str(self.id)


STATUS_CHOICES = (
    ('Accepted','Accepted'),
    ('Cooking', 'Cooking'),
    ('On the way','On the way'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel')
)

class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default= '')

    



