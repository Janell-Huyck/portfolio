from django.urls import path
from projects import views

urlpatterns = [
    path("", views.index, name="home"),
    path("featured", views.featured, name="featured"),
    path("frontend", views.front_end, name="frontend"),
    path("backend", views.back_end, name="backend"),
    path("<slug:slug>", views.projectDetail, name="project_detail"),
]
