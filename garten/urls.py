from django.urls import path
from . import views

urlpatterns=[
      path('',views.index),
      path('index.html',views.index),
      path('register.html',views.register),
      path('login.html',views.login),
      path('application.html',views.application),
      path('about.html',views.about),
      path('register',views.registerform),
      path('login',views.loginform),
      path('logout',views.logout),
      path('apply',views.applyform)
]