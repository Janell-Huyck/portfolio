from django.shortcuts import render
from projects.models import Project

from projects.display_text import intro1, intro2, intro3, skills


def index(request):
    profile_image_url = "../static/janell-webcam-no-background.png"
    featured_projects = Project.objects.filter(is_featured=True)[0]
    front_end_projects = (
        Project.objects.filter(language__in=["RR", "RE", "JS"])
        .filter(is_featured=False)
        .order_by("display_order")
    )
    back_end_projects = (
        Project.objects.filter(language__in=["DJ", "PY"])
        .filter(is_featured=False)
        .order_by("display_order")
    )

    context = {
        "profile_image_url": profile_image_url,
        "intro1": intro1,
        "intro2": intro2,
        "intro3": intro3,
        "skills": skills,
        "featured": featured_projects,
        "back_end_projects": back_end_projects,
        "front_end_projects": front_end_projects,
    }
    html = "index.html"
    return render(request, html, context)


def projectDetail(request, slug):
    project = Project.objects.get(slug=slug)
    context = {
        "project": project,
    }
    html = "project_detail.html"
    return render(request, html, context)
