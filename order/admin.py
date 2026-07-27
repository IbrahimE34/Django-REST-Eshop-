from django.contrib import admin

from order.models import Cart, Order, CartItem, OrderItem


# from order.models import *
# admin.site.register(CartItem)
# admin.site.register(Cart)
#
# admin.site.register(Order)
# admin.site.register(OrderItem)

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner','created_at')
    search_fields = ('owner__username','owner__emai')
    ordering = ('-created_at',)

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'cart', 'product', 'quantity')
    search_fields = ('product__name',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner','status', 'created_at')
    list_filter = ('status','created_at')
    search_fields = ('owner__username','owner__emai')
    ordering = ('-created_at',)

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "order",
        "product",
        "quantity",
        "price",)
    search_fields = ('product__name',)