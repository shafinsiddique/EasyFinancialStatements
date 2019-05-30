from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path("", views.home, name='analyzer-home'),
    path("compare/", views.compare, name='analyzer-compare')
]
