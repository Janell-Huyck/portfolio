from django.shortcuts import render
from projects.models import Project

from projects.display_text import intro1, intro2, intro3, skills


def index(request):

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

    # javascript_projects = Project.objects.filter(language="JS").filter(
    #     is_featured=False
    # )
    # django_projects = Project.objects.filter(language="DJ").filter(is_featured=False)
    # react_projects = Project.objects.filter(language="RE").filter(is_featured=False)
    # react_redux_projects = Project.objects.filter(language__in=["RR", "RE"]).filter(
    #     is_featured=False
    # )
    # python_projects = Project.objects.filter(language="PY").filter(is_featured=False)

    context = {
        "intro1": intro1,
        "intro2": intro2,
        "intro3": intro3,
        "skills": skills,
        "featured": featured_projects,
        "project_types": [
            {"projects": back_end_projects, "description": "Django/Python"},
            {
                "projects": front_end_projects,
                "description": "React, React/Redux, JavaScript",
            },
            # {"projects": django_projects, "description": "Django Projects"},
            # {"projects": python_projects, "description": "Python Projects"},
            # {"projects": react_projects, "description": "React Projects"},
            # {
            #     "projects": react_redux_projects,
            #     "description": "React / React-Redux Projects",
            # },
            # {"projects": javascript_projects, "description": "JavaScript Projects"},
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
