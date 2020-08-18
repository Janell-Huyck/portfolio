from django.shortcuts import render
from projects.models import Project

from projects.display_text import intro1, intro2


def index(request):
    profile_image_url = "../static/janell-webcam-no-background.png"

    context = {
        "profile_image_url": profile_image_url,
        "intro1": intro1,
        "intro2": intro2,
    }
    html = "index.html"
    return render(request, html, context)


def featured(request):
    html = "featured.html"
    featured = Project.objects.filter(is_featured=True)[0]
    context = {"featured": featured}
    return render(request, html, context)


def front_end(request):
    html = "frontend.html"
    projects = (
        Project.objects.filter(language__in=["RR", "RE", "JS"])
        .filter(is_featured=False)
        .order_by("display_order")
    )
    context = {"projects": projects}
    return render(request, html, context)


def back_end(request):
    html = "backend.html"
    projects = (
        Project.objects.filter(language__in=["DJ", "PY"])
        .filter(is_featured=False)
        .order_by("display_order")
    )
    context = {"projects": projects}
    return render(request, html, context)


def projectDetail(request, slug):
    project = Project.objects.get(slug=slug)
    context = {
        "project": project,
    }
    html = "project_detail.html"
    return render(request, html, context)


def error404(request, exception):
    return render(request, "404.html", status=404)


def error500(request):
    return render(request, "500.html", status=500)
