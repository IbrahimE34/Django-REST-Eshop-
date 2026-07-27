from django.contrib.auth.views import LoginView
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from user.views import *




urlpatterns = [
    path("register/", Register.as_view()),
    path("login/", LoginView.as_view()),

]