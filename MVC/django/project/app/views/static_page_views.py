from django.shortcuts import render


def home(request):
    return render(request, 'app/static_pages/home.html')


def help(request):
    return render(request, 'app/static_pages/help.html')


def about(request):
    return render(request, 'app/static_pages/about.html')


def contact(request):
    return render(request, 'app/static_pages/contact.html')
