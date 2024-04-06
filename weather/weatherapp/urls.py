from django.urls import path
from .import views

urlpatterns = [
<<<<<<< HEAD
    path('',views.page),
    path('page', views.home),
=======
    path('render', views.home),
    path('', views.page),
>>>>>>> upstream/main
]