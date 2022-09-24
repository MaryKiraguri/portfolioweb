from django.http import HttpResponse
def index(request):
    return HttpResponse('We made it this far!')
    