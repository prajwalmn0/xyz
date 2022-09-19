from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('/',views.account),
    path('signup',views.signup),
    path('login',views.login),
]