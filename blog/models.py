from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("home")


class Post(models.Model):
    title = models.CharField(max_length=200)
    body = RichTextField(blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    category = models.ManyToManyField("Category", related_name="post_category")
    picture_1 = models.FilePathField(
        path="static/img/blog", recursive=True, null=True, blank=True
    )
    picture_2 = models.FilePathField(
        path="static/img/blog", recursive=True, null=True, blank=True
    )
    picture_3 = models.FilePathField(
        path="static/img/blog", recursive=True, null=True, blank=True
    )
    picture_4 = models.FilePathField(
        path="static/img/blog", recursive=True, null=True, blank=True
    )

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def get_categories(self):
        return ",".join([str(cat) for cat in self.category.all()])

    def __str__(self):
        return self.title
