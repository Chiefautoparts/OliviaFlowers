# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
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
	image = models.ImageField(blank=True)
	desc = models.TextField()
	price = models.DecimalField(max_digits=10, decimal_places=2)
	availablity = models.BooleanField(default=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ('name',)
		index_together = (('id', 'slug'),)

	def __str__(self):
		return self.name

class OrderManager(models.Manager):
	def orderValidation(self, postData):
		status = {'valid':True, 'errors':[]}



class Order(models.Model):
	firstName = models.CharField(max_length=200)
	lastName = models.CharField(max_length=200)
	phoneNum = models.IntegerField()
	email = models.CharField(max_length=255)
	delivery = models.BooleanField(default=False)
	address = models.CharField(max_length=255, blank=True)
	products = models.ForeignKey(Product, related_name="products")
	date_requested = models.DateField(blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = OrderManager()



