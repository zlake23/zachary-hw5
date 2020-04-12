import requests
from django.shortcuts import render

def home(request):
    context = {
        "active_home": "active",
    }
    return render(request, "about.html", context)


def blog(request):
    context = {
        "active_blog": "active",
    }
    return render(request, "blog.html", context)

def contact(request):
    context = {
        "active_contact": "active",
    }
    return render(request, "contact.html", context)

def projects(request):
    context = {
        "active_projects": "active",
    }
    return render(request, "projects.html", context)