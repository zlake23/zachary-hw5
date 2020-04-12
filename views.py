import requests
from django.shortcuts import render

def home(request):
    about_html = open("content/about.html").read()
    context = {
        "content": about_html,
        "title": "Home Page",
        "active_home": "active",
    }
    return render(request, "base.html", context)


def blog(request):
    blog_html = open("content/blog.html").read()
    context = {
        "content": blog_html,
        "title": "My Blog",
        "active_blog": "active",
    }
    return render(request, "base.html", context)

def contact(request):
    contact_html = open("content/contact.html").read()
    context = {
        "content": contact_html,
        "title": "Contact Page",
        "active_contact": "active",
    }
    return render(request, "base.html", context)

def projects(request):
    projects_html = open("content/projects.html").read()
    context = {
        "content": projects_html,
        "title": "My Projects",
        "active_projects": "active",
    }
    return render(request, "base.html", context)