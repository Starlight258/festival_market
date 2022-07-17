from django.contrib import admin

from .models import yeosuRestaurant, jeonjuRestaurant, product, productdetail, wandoRestaurant

# Register your models here.
admin.site.register(yeosuRestaurant)
admin.site.register(jeonjuRestaurant)
admin.site.register(product)
admin.site.register(productdetail)
admin.site.register(wandoRestaurant)