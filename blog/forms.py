from django import forms
from blog.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            "title",
            "tag",
            "body",
            "snippet",
            "picture_1",
            "picture_1_text",
            "picture_2",
            "picture_2_text",
            "picture_3",
            "picture_3_text",
            "picture_4",
            "picture_4_text",
        )

        widgets = {"snippet": forms.Textarea(attrs={"class": "form-control"})}
