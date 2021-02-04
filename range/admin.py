from django.contrib import admin

# Register your models here.



from .models import TypeGoods, GoodsShopList

# Register your models here.
admin.site.register(TypeGoods)
admin.site.register(GoodsShopList)