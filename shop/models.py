from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.template.defaultfilters import slugify

class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="Categories")

    def __str__(self):
        return self.name
 

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0) 
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    slug = models.SlugField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=1000, default=" ", null=True, blank=True)
    image = models.ImageField(upload_to= 'uploads/products/')

    def __str__(self):
        return self.name


class Customer(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    
    def __str__(self):
        return self.username
    
class OrderItem(models.Model) :
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)


    def __str__(self):
        return f"{self.quantity} of {self.item.name}"   

class Order(models.Model) :
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem, blank=True)
    ordered_date = models.DateTimeField()
    
    def __str__(self):
        return self.user.username
    

def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.name)


pre_save.connect(slug_generator, sender= Product)