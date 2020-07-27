from django.shortcuts import render
from projects.models import Project

from projects.display_text import intro1, intro2, intro3, skills


def index(request):

    javascript_projects = Project.objects.filter(language="JS")
    django_projects = Project.objects.filter(language="DJ")
    react_projects = Project.objects.filter(language="RE")
    react_redux_projects = Project.objects.filter(language="RR")
    python_projects = Project.objects.filter(language="PY")

    context = {
        "intro1": intro1,
        "intro2": intro2,
        "intro3": intro3,
        "skills": skills,
        # "javascript_projects": javascript_projects,
        # "django_projects": django_projects,
        # "react_projects": react_projects,
        # "react_redux_projects": react_redux_projects,
        # "python_projects": python_projects,
        "project_types": [
            {"projects": javascript_projects, "description": "JavaScript Projects"},
            {"projects": react_projects, "description": "React Projects"},
            {"projects": react_redux_projects, "description": "React-Redux Projects"},
            {"projects": python_projects, "description": "Python Projects"},
            {"projects": django_projects, "description": "Django Projects"},
        ],
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
