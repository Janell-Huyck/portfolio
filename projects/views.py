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

    context["intro3"] = """HTML | CSS | JavaScript | Python | Django"""

    context[
        "intro4"
    ] = """But that doesn't even scratch
        the surface of what I\'ve learned so far..."""

    context["technology1"] = [
        "• Agile and Scrum",
        "• API’s",
        "• Async operations",
        "• Clean coding",
        "• Decorator functions",
        "• Git and version control",
    ]
    context["technology2"] = [
        "• GitLab and GitHub",
        "• Google-Fu",
        "• Group projects",
        "• Heroku",
        "• Logging",
        "• Long-running programs",
    ]
    context["technology3"] = [
        "• Modules",
        "• MySQL",
        "• Pipenv",
        "• Poetry",
        "• Pyenv",
        "• PythonAnyhere",
    ]
    context["technology4"] = [
        "• React, React/Redux",
        "• SQLite",
        "• Terminal commands",
        "• Ubuntu / Windows/ Mac familiarity",
        "• Virtual environments",
        "• VS Code",
    ]

    context["intro5"] = "Here are a few of my favorite projexts."
    context["projects"] = Project.objects.all()
    html = "index.html"
    return render(request, html, context)


def projectDetail(request, slug):
    context = {}
    project = Project.objects.get(slug=slug)
    context["project"] = project
    html = "project_detail.html"
    return render(request, html, context)