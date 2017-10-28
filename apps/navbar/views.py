# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

def navbar(request):
	return render(request, 'navbar/nav.html')