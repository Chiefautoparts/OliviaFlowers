# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.
def index(request):
	print '**services**' * 200
	return render(request, 'services/services.html')

def events(request):
	print '**events**' * 250

def designs(request):
	print '**designs**' * 250

def seasonal(request):
	print '**seasonal**' * 250