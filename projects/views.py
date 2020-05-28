from django.shortcuts import render
from projects.models import Project


def index(request):
    context = {}
    context[
        "intro1"
    ] = """Hi.  I\'m Janell Huyck.  That\'s pronounced like
        \"hike\", if you were wondering.  I started coding in 2019 at Kenzie
        Academy with their Full Stack Web Development/ Software Engineering
        program.  That\'s a 12-month intensive training program that teaches
        not just coding skills, but how to learn new languages and
        frameworks."""

    context[
        "intro2"
    ] = """Most recently, I’ve been working on projects
        in Django, like this site."""

    context["intro3"] = "Here are a few of my favorite projects."

    context["skills"] = [
        "• Agile and Scrum",
        "• API’s",
        "• Async operations",
        "• Clean coding",
        "• Decorator functions",
        "• Git and version control",
        "• GitLab and GitHub",
        "• Google-Fu",
        "• Group projects",
        "• Heroku",
        "• Logging",
        "• Long-running programs",
        "• Modules (use and creation)",
        "• Pipenv",
        "• Poetry",
        "• Pyenv",
        "• PythonAnyhere",
        "• React, React/Redux",
        "• SQLite",
        "• Terminal commands / CLI",
        "• Ubuntu / Windows/ Mac familiarity",
        "• Virtual environments",
        "• VS Code",
    ]

    all_projects = Project.objects.all().order_by("languages")
    javascript_projects = []
    for i in range(3):
        javascript_projects.append(all_projects[i])
    context["javascript_projects"] = javascript_projects
    django_projects = []
    for i in range(3, all_projects.count()):
        django_projects.append(all_projects[i])
    context["django_projects"] = django_projects
    html = "index.html"
    return render(request, html, context)


def projectDetail(request, slug):
    context = {}
    project = Project.objects.get(slug=slug)
    context["project"] = project
    html = "project_detail.html"
    return render(request, html, context)
