from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('portal/', views.portal, name='portal'),
    path('add/', views.add, name='add'),
    path('logout/',views.logout, name='logout'),
    path('database/',views.database,name='database')
]