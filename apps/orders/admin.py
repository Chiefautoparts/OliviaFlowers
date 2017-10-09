# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Category, Product
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug']
	prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug', 'price', 'availablity', 'created_at', 'updated_at']
	list_filter = ['availablity', 'created_at', 'updated_at']
	list_editable = ['price', 'availablity']
	prepopulated_fields = {'slug': ('name', )}
admin.site.register(Product, ProductAdmin)