from django.contrib import admin

from .models import Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')  # Display these fields in the admin panel
    search_fields = ('name', 'description')  # Enable search functionality
    list_filter = ('price',)  # Add filter options

admin.site.register(Product, ProductAdmin)
