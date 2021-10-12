from django.contrib import admin
from .models import Product
from django.utils.html import format_html

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" />'.format(object.product_photo.url))

    thumbnail.short_description = 'Product Image'
    list_display = ('id', 'thumbnail', 'product_title', 'state', 'color', 'model', 'year', 'body_style', 'fuel_type', 'is_featured')
    list_display_links = ('id', 'thumbnail', 'product_title')
    list_editable = ('is_featured',)
    search_fields = ('id', 'product_title', 'city', 'model', 'body_style', 'fuel_type')
    list_filter = ('city', 'model', 'body_style', 'fuel_type')

admin.site.register(Product, ProductAdmin)
