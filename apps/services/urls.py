from django.conf.urls import url
from . import views

app_name='services'
urlpatterns = [
	url(r'^$', views.index, name='main')
]