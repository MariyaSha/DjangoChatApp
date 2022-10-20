from django.urls import path
from . import views

from django.conf.urls import url

urlpatterns = [
	path('', views.myview),
	path('login/', views.login),
	path('send_chat/', views.send_chat),
	path('sign_up/', views.sign_up),
	path('create_user/', views.create_user)
	]