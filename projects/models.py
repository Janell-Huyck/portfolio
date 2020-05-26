from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify


class Project(models.Model):
    slug = models.SlugField(null=False, unique=True)
    title = models.CharField(max_length=50)
    synopsis = models.TextField(null=True, blank=True)
    languages = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    site_url = models.URLField(null=True, blank=True)
    picture_1 = models.FilePathField(
        path="static/img", recursive=True, null=True, blank=True
    )
    picture_2 = models.FilePathField(
        path="static/img", recursive=True, null=True, blank=True
    )
    picture_3 = models.FilePathField(
        path="static/img", recursive=True, null=True, blank=True
    )
    picture_4 = models.FilePathField(
        path="static/img", recursive=True, null=True, blank=True
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("project_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
