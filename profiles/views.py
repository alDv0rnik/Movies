import logging
from .decorators import unauthenticated_user
from .forms import CreateUserForm

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


logger = logging.getLogger('movie_logger')


@unauthenticated_user
def login_user(request):
    # breakpoint()
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.info(request, 'Username or password do not match')
            logger.info('Username or password do not match')
    return render(request, "login.html")


@unauthenticated_user
def register_user(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            messages.info(request, f"The user with username {username} has been registered")
            return redirect("login")
    context = {
        "form": form
    }
    return render(request, "register.html", context=context)


def logout_user(request):
    logout(request)
    return redirect("home")
