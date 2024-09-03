from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'price', 'category', 'image']

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'quantity']

@admin.register(Carts)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'quantity']

@admin.register(ShippingAddress)
class ShippingAdmin(admin.ModelAdmin):
    list_display = ['user', 'full_name', 'email', 'phone_no', 'country', 'division', 'district', 'address1', 'address2', 'thana', 'zipcode']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'full_name', 'email', 'shipping_address', 'amount_paid', 'date_order']
@admin.register(OrderItem)
class OrderItemsAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'user', 'quantity', 'price']