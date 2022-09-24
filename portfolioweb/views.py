from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return HttpResponse('We made it this far!')

def user(request):
    return HttpResponse('Hello user')

def portfolio(request):
    return render(request, 'portfolioweb/index.html')