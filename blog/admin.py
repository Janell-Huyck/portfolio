from django.contrib import admin
from blog.models import Post, Category


class PostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "get_categories",
        "body",
        "created_date",
        "published_date",
    )


admin.site.register(Post, PostAdmin)

admin.site.register(Category)
