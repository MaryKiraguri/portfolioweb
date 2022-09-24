from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    return render(request, 'portfolioweb/index.html')

def services(request):
    return render(request, 'portfolioweb/services.html')


def testimonials(request):
    return render(request, 'portfolioweb/testimonials.html')

def contacts(request):
    return render(request, 'portfolioweb/contacts.html')
