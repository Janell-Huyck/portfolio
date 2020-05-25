from django.contrib import admin
from projects.models import Project


class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "synopsis",
        "languages",
        "description",
        "role",
        "site_url",
        "repository",
        "group_project",
        "created",
        "picture_1",
        "picture_2",
        "picture_3",
        "picture_4",
    )
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Project, ProjectAdmin)
