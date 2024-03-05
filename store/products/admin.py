from django.contrib import admin

from users.models import User

from products.models import ProductCategory, Product

admin.site.register(Product)
admin.site.register(ProductCategory)
