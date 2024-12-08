from django.contrib import admin
from app.models import Product,Customer

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','title','selling_price','discounted_price','category','product_image','create_at','update_at']


@admin.register(Customer)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','user','locality','city','state','zipcode']
