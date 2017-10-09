# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=255, db_index=True)
	slug = models.SlugField(max_length=255, db_index=True)

	class Meta:
		ordering = ('name',)
		verbose_name='category'
		verbose_name_plural = 'categories'

	def __str__(self):
		return self.name	

class Product(models.Model):
	category = models.ForeignKey(Category, related_name='products')
	name = models.CharField(max_length=255, db_index=True)
	slug = models.SlugField(max_length=255, db_index=True)
	image = models.ImageField(upload_to='orders/%Y/%m/%d', blank=True)
	desc = models.TextField(blank=True)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	availablity = models.BooleanField(default=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ('name',)
		index_together = (('id', 'slug'),)

	def __str__(self):
		return self.name
	