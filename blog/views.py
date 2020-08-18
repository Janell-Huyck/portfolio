from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .forms import PostForm
from django.shortcuts import redirect

from blog.models import Post


def index(request):
    html = "blog/index.html"
    post = (
        Post.objects.filter(published_date__lte=timezone.now())
        .order_by("-published_date")
        .first()
    )
    if post:
        context = {"post": post}
    else:
        context = {}
    return render(request, html, context)


def all(request):
    html = "blog/all.html"
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by(
        "-published_date"
    )
    context = {"posts": posts}
    return render(request, html, context)


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "blog/detail.html", {"post": post})


def new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect("detail", pk=post.pk)
    else:
        form = PostForm()
    return render(request, "blog/edit.html", {"form": form})


def edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect("detail", pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, "blog/edit.html", {"form": form})


def newest():
    pass

