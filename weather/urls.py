
from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.index),
#locating index function in views file
]