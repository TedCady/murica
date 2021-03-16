from django.urls import path
from . import views

urlpatterns=[
    path('', views.index),
    path('airForce', views.AF),
    path('army', views.Army),
    path('coastGuard', views.Coast),
    path('marines', views.Marines),
    path('navy', views.Navy),
    path('about', views.info),
    path('register', views.register),
    path('login', views.login),
    path('contact', views.contact),
    path('welcome', views.welcome),
    path('reg', views.reg),
    path('logout', views.logout),
    path('loginVal', views.loginVal),
    path('contactUs', views.contactUS)
]
