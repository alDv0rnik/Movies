import logging
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


logger = logging.getLogger('movie_logger')


def login_user(request):
    # breakpoint()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(
            request,
            username=username,
            password=password
        )
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            logger.info('Username or password do not match')
    return render(request, 'login.html')
