from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.urls import reverse


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("home")


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = RichTextField(blank=True, null=True)
    snippet = models.CharField(max_length=255, null=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    tag = models.ManyToManyField(Tag, blank=True)

    picture_1 = models.FilePathField(
        path="static/img/blog", recursive=True, null=True, blank=True
    )
    picture_1_text = models.CharField(max_length=200, blank=True, null=True)
    picture_2 = models.FilePathField(
        path="static/img/blog", recursive=True, null=True, blank=True
    )
    picture_2_text = models.CharField(max_length=200, blank=True, null=True)
    picture_3 = models.FilePathField(
        path="static/img/blog", recursive=True, null=True, blank=True
    )
    picture_3_text = models.CharField(max_length=200, blank=True, null=True)
    picture_4 = models.FilePathField(
        path="static/img/blog", recursive=True, null=True, blank=True
    )
    picture_4_text = models.CharField(max_length=200, blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def get_categories(self):
        return ",".join([str(cat) for cat in self.tag.all()])

    def __str__(self):
        return self.title
