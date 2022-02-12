from django.shortcuts import render

def page_view(request):
    return render(request, 'pages/index.html')


def about_view(request):
    return render(request, 'pages/about.html')


def services_view(request):
    return render(request, 'pages/services.html')

def contact_view(request):
    return render(request, 'pages/contact.html')
