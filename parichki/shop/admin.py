from django.contrib import admin
from .models import Product, Category

#Регистрируем табличку Category в панели админа

admin.site.register(Product),
admin.site.register(Category),