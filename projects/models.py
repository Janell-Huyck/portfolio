from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify


class Project(models.Model):
    JAVASCRIPT = "JS"
    DJANGO = "DJ"
    LANGUAGE_CHOICES = [
        ("JS", "JavaScript"),
        ("DJ", "Django"),
    ]
    slug = models.SlugField(null=False, unique=True, editable=False)
    title = models.CharField(max_length=50)
    synopsis = models.TextField(null=True, blank=True)
    language = models.CharField(
        max_length=2, choices=LANGUAGE_CHOICES, null=True, blank=True
    )
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
