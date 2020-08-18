from django.urls import path
from blog import views

urlpatterns = [
    path("", views.index, name="blog"),
    path("newest/", views.newest, name="newest"),
    path("all/", views.all, name="all"),
    path("new/", views.new, name="new"),
    path("<int:pk>/", views.detail, name="detail"),
    path("<int:pk>/edit", views.edit, name="edit"),
]
