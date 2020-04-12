import requests
from django.shortcuts import render

def home(request):
    about_html = open("content/about.html").read()
    context = {
        "content": about_html,
    }
    return render(request, "base.html", context)


def blog(request):
    blog_html = open("content/blog.html").read()
    context = {
        'content': blog_html,
    }
    return render(request, "base.html", context)

def contact(request):
    contact_html = open("content/contact.html").read()
    context = {
        'content': contact_html,
    }
    return render(request, "base.html", context)

def projects(request):
    projects_html = open("content/projects.html").read()
    context = {
        'content': projects_html,
    }
    return render(request, "base.html", context)