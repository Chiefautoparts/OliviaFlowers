# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.
def index(request):
	print '**INDEX**' * 250
	return render(request, 'home/index.html')