from django.shortcuts import render, HttpResponse


def index(request):
    return HttpResponse("<h3>Main page</h3>")
