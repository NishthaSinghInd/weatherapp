from django.urls import path
from .import views

urlpatterns = [
    path('render', views.home),
    path('', views.page),
]