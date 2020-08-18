from django import forms
from blog.models import Post, Category

category_choices = Category.objects.all().values_list("name", "name")
category_choice_list = [choice for choice in category_choices]


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            "title",
            "category",
            "body",
            "picture_1",
            "picture_2",
            "picture_3",
            "picture_4",
        )

        # widgets = {
        #     "category": forms.Select(
        #         choices=category_choice_list, attrs={"class": "form-control"}
        #     )
        # }

