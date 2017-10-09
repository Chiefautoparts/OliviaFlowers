# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def index(request):
	print '**services**' * 200
	return render(request, 'services/services.html')