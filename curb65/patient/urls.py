from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
	path('',views.index,name="index"),
    path('score/<str:patient_id>/', views.score, name='score'),
    path('search/', views.search, name='search'),
]