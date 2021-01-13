from django.contrib import admin
from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path("", views.home, name="home"),
    path("register/", views.register,name="register"),
    path("login/", views.login_request, name="login"),
    path("logout/", views.logout_request, name="logout"),
    path("profile/", views.profile, name="profile"),
    path("edit_profile/", views.edit_profile, name="edit_profile"),
    path("about/", views.about, name="about"),
    path("change_password/", views.change_password, name="change_password")
]
