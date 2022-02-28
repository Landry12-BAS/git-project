from django.shortcuts import render
from .models import Team

def page_view(request):
    teams = Team.objects.all()
    data = {
        'teams': teams,
    }
    return render(request, 'pages/index.html', data)


def about_view(request):
    teams = Team.objects.all()
    data = {
        'teams': teams,
    }
    return render(request, 'pages/about.html', data)


def services_view(request):
    return render(request, 'pages/services.html')

def contact_view(request):
    return render(request, 'pages/contact.html')
