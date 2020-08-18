from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .forms import PostForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView

from blog.models import Post, Category


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


def categoryView(request, cats):
    html = "blog/categories.html"
    category_posts = Post.objects.filter(category__name__icontains=cats)
    context = {"category_posts": category_posts, "cats": cats}
    return render(request, html, context)


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "blog/detail.html", {"post": post})


@login_required
def new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = timezone.now()
            post.save()
            return redirect("detail", pk=post.pk)
    else:
        form = PostForm()
    return render(request, "blog/edit.html", {"form": form})


@method_decorator(login_required, name="dispatch")
class AddCategoryView(CreateView):
    model = Category
    template_name = "blog/add_category.html"
    fields = "__all__"


@login_required
def edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = timezone.now()
            post.save()
            return redirect("detail", pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, "blog/edit.html", {"form": form})
