from django.conf.urls import url
from . import views

app_name='orders'
urlpatterns = [
	url(r'^$', views.orderForm, name='orderForm'),
	url(r'^catalog$', views.catalog, name='catalog'),
	url(r'^submit$', views.submit, name='submit')
]