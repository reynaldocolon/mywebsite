from django.shortcuts import render
from .models import ContactMessage, Project

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def projects(request):
    all_projects = Project.objects.all().order_by('-created_at')
    return render(request, "projects.html", {"projects": all_projects})

def resources(request):
    return render(request, "resources.html")

def contact(request):
    submitted = False
    if request.method == "POST":
        ContactMessage.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            message=request.POST.get("message")
        )
        submitted = True
    return render(request, "contact.html", {"submitted": submitted})
