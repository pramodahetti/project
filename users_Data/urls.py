from . import views
from django.urls import path,include
urlpatterns = [
    path('',views.home),
    path('login',views.login),
    path('about',views.about),
    path('register',views.register),
    path('log',views.logged),
]