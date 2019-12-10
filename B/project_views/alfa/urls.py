from django.urls import path,include
from django.contrib import admin
from . import views

urlpatterns= [
    path('', views.index, name='index'),

    path('blog', views.blog, name='blog'),

    path('mentee', views.mentee, name='mentee'),
    
    path('mentor', views.mentor, name='mentor'),

    path('author', views.author, name='author'),
    ]