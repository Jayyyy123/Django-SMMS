from django.urls import path
from . import views

# general/details

urlpatterns = [
    path('', views.registerPage, name="register")
]
