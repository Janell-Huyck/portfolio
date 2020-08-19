from django.urls import path
from blog import views

urlpatterns = [
    path("", views.index, name="blog"),
    path("new/", views.new, name="new"),
    path("add_tag/", views.AddTagView.as_view(), name="add_tag"),
    path("tag/<str:tag>/", views.tagView, name="tag"),
    path("<int:pk>/", views.detail, name="detail"),
    path("<int:pk>/edit", views.edit, name="edit"),
]
