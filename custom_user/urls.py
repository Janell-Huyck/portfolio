from django.urls import path
from custom_user import views


urlpatterns = [
    path("", views.index, name="home"),
    path("login_page/", views.loginView, name="loginPage"),
    path("logout_page/", views.logoutView, name="logoutPage"),
    path("signup_page/", views.signupView, name="signupPage"),
]
