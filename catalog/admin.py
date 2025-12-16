from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Configuring the Category model display in the admin panel.
    """
    list_display = ('id', 'name',)
    search_fields = ('name', 'description',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Configuring the display of the Product model in the admin panel.
    """
    list_display = ('id', 'name', 'price', 'category',)
    list_filter = ('category',)
    search_fields = ('name', 'description',)
    list_display_links = ('id', 'name',)