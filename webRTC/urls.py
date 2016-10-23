from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from flockathon import views

urlpatterns = [
	url(r'^register', views.send, name='register'),
	url(r'^saveFile', views.saveFile, name='saveFile'),
	url(r'^screen', views.screen, name='screen'),
	url(r'^myflockathon/(?P<pk>\d+)/(?P<user_name>[\w\-]+)$',login_required(views.IndexView.as_view()),name='myflockathon'),
	
]
