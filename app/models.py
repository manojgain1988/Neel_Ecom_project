from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    CATEGORY_CHOICES = (
        ('ML' , 'Milk'),
        ('CR' , 'Curd'),
        ('LS' , 'Lassi'),
        ('MS' , 'Milkshake'),
        ('PN' , 'Paneer'),
        ('GH' , 'Ghee'),
        ('CZ' , 'Cheese'),
        ('IC' , 'Ice_Creams'),  
    )
    
    title = models.CharField( max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    composition = models.TextField(default = '')
    prodapp = models.TextField(default = '')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image = models.ImageField(upload_to='product/')
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    
class Customer(models.Model):
    STATE_CHOICES = (
        ('Dhaka' , 'Dhaka'),
        ('Chittragram' , 'Chittragram'),
        ('Khulna' , 'Khulna'),
        ('Barishal' , 'Barishal'),
        ('Jessore' , 'Jessore'),
        ('Rajshahi' , 'Rajshahi'),
        ('Sylhet' , 'Sylhet'),
        ('Gopalganj' , 'Gopalganj'),
        ('Faridpur' , 'Madaripur'),
        ('Madaripur' , 'Faridpur'),
        ('Bagherhat' , 'Bagherhat'),
        ('Kotalipara' , 'Kotalipara'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=True, null=True)
    locality = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    mobile = models.IntegerField(default=0)
    zipcode = models.IntegerField()
    state = models.CharField(max_length=100, blank=True, null=True,choices=STATE_CHOICES)
    
    def __str__(self):
        return self.name
    