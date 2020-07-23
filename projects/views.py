from django.shortcuts import render
from projects.models import Project

from projects.display_text import intro1, intro2, intro3, skills


def index(request):

    javascript_projects = Project.objects.filter(language="JS")
    django_projects = Project.objects.filter(language="DJ")

    context = {
        "intro1": intro1,
        "intro2": intro2,
        "intro3": intro3,
        "skills": skills,
        "javascript_projects": javascript_projects,
        "django_projects": django_projects,
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
