from django.contrib import admin
from catalog.models import Category, Product, Trademark


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','status','created_at','updated_at')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('sku','name','price','trademark','category','status','created_at','updated_at',)    

class TrademarkAdmin(admin.ModelAdmin):
    list_display = ('name','status','created_at','updated_at',)    

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Trademark, TrademarkAdmin)