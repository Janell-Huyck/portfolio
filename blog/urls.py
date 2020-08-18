from django.urls import path
from blog import views

urlpatterns = [
    path("", views.index, name="blog"),
    path("new/", views.new, name="new"),
    path("add_category/", views.AddCategoryView.as_view(), name="add_category"),
    path("category/<str:cats>/", views.categoryView, name="category"),
    path("<int:pk>/", views.detail, name="detail"),
    path("<int:pk>/edit", views.edit, name="edit"),
]
