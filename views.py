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
    response = requests.get('https://api.github.com/users/zlake23/repos')
    repos = response.json()
    context = {
        "active_projects": "active",
        'github_repos': repos,
    }
    return render(request, "projects.html", context)