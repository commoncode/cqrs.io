from django.contrib import admin

from ecommerce.models import Product, ProductAdmin, Cart, CartAdmin, Oplogqueue, OplogqueueAdmin
# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(Oplogqueue, OplogqueueAdmin)




