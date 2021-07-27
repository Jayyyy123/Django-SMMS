from django.urls import path
from . import views

# general/details

urlpatterns = [
    path('home/', views.userBooking, name="userBooking"),
    path('cancel/', views.userCancel, name="userCancel"),
    path('history/', views.userHistory, name="userHistory"),
    path('profile/', views.userProfile, name="userProfile"),
    path('register/', views.registerPage, name="register"),
    path('login/', views.logInPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('order/', views.createOrder, name="order"),
]
