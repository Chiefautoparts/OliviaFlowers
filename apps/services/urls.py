from django.conf.urls import url
from . import views
from django.contrib import messages
from ..orders.models import Product

app_name='services'
urlpatterns = [
	url(r'^$', views.index, name='main'),
	url(r'^events$', views.events, name='events'),
	url(r'^designs$', views.designs, name='designs'),
	url(r'^seasonal$', views.seasonal, name='seasonal')
]