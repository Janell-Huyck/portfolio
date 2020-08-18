from django.contrib import admin
from blog.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "text",
        "created_date",
        "published_date",
    )


admin.site.register(Post, PostAdmin)
