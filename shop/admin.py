from django.contrib import admin
from .models import Product, Customer, Category, Order, OrderItem

# Register your models here.
class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price','category']

class AdminCategory(admin.ModelAdmin):
    list_display = ['name']

class AdminOrder(admin.ModelAdmin):
    list_display = ['user','ordered_date']

class AdminOrderItem(admin.ModelAdmin):
    list_display = ['user','ordered','item', 'quantity']

admin.site.register(Product,AdminProduct)
admin.site.register(Category,AdminCategory)
admin.site.register(Customer)
admin.site.register(Order,AdminOrder)
admin.site.register(OrderItem,AdminOrderItem)
