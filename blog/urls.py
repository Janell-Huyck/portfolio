from django.urls import path
from projects import views

urlpatterns = [
    path("newest", views.newest, name="newest"),
    path("all", views.all, name="all"),
    path("<slug:slug>", views.detail, name="detail"),
]
