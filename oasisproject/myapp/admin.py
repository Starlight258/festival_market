from django.contrib import admin

from .models import yeosuRestaurant, jeonjuRestaurant, product, productdetail, wandoRestaurant,wandoVisit, yeosuVisit, jeonjuVisit, goheungVisit, gwangyangVisit, gwangyangRestaurant, goheungRestaurant

# Register your models here.
admin.site.register(yeosuRestaurant)
admin.site.register(jeonjuRestaurant)
admin.site.register(product)
admin.site.register(productdetail)
admin.site.register(wandoRestaurant)
admin.site.register(wandoVisit)
admin.site.register(yeosuVisit)
admin.site.register(jeonjuVisit)
admin.site.register(goheungVisit)
admin.site.register(gwangyangVisit)
admin.site.register(gwangyangRestaurant)
admin.site.register(goheungRestaurant)