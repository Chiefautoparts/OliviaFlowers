# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.
def catalog(request):
	print '**ordersindex**' * 250
	return render(request, 'orders/shopFlowers.html')

def orderForm(request):
	print '**orderForm**' * 250
	return render(request, 'orders/order.html')

def submit(request):
	print '**OrderSubmitted**' * 250
	return redirect('orders:orderForm')