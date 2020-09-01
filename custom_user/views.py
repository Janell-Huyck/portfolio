from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate
from django.shortcuts import render
from portfolio import settings
from custom_user.forms import LoginForm, CustomUserForm
from custom_user.models import CustomUser


# @login_required
# def index(request):
#     context = {"settings": settings.AUTH_USER_MODEL}
#     return render(request, "index.html", context)


def logoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse("loginPage"))


def loginView(request):
    message_after = ""
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data["username"], password=data["password"]
            )
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(request.GET.get("next", reverse("home")))
            else:
                message_after = """Credentials supplied do not match our records.
                   Please try again."""
    form = LoginForm()
    return render(
        request, "general_form.html", {"form": form, "message_after": message_after}
    )


def signupView(request):
    context = {}
    if request.method == "POST":
        form = CustomUserForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = CustomUser.objects.create(
                username=data["username"],
                password=data["password"],
                display_name=data["display_name"],
            )
            new_user.set_password(raw_password=data["password"])
            new_user.save()
            user = authenticate(
                request, username=data["username"], password=data["password"]
            )
            if user:
                login(request, user)
            return HttpResponseRedirect(reverse("home"))
        else:
            context["form"] = form
    else:
        form = CustomUserForm()
        context["form"] = form
    return render(request, "general_form.html", context)
