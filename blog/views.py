from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .forms import PostForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView

from blog.models import Post, Tag


def index(request):
    html = "blog/index.html"
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by(
        "-published_date"
    )
    if posts:
        context = {"posts": posts}
    else:
        context = {}
    return render(request, html, context)


def tagView(request, tag):
    html = "blog/tags.html"
    tag_posts = Post.objects.filter(tag__name__icontains=tag)
    if tag_posts:
        context = {"tag_posts": tag_posts, "tag": tag}
    else:
        context = {"tag": tag}
    return render(request, html, context)


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "blog/detail.html", {"post": post})


@login_required
def new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = timezone.now()
            post.save()
            form.save_m2m()
            return redirect("detail", pk=post.pk)
    else:
        form = PostForm()
    return render(request, "blog/edit.html", {"form": form})


@method_decorator(login_required, name="dispatch")
class AddTagView(CreateView):
    model = Tag
    template_name = "blog/add_tag.html"
    fields = "__all__"


@login_required
def edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = timezone.now()
            post.save()
            form.save_m2m()
            return redirect("detail", pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, "blog/edit.html", {"form": form})
