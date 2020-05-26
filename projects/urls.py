from django.urls import path
from projects import views

urlpatterns = [
    path("", views.index, name="home"),
    path("<slug:slug>", views.projectDetail, name="project_detail"),
]
