from django.http import HttpResponse


# Create your views here.

def index(request):
    return HttpResponse('Hello, this is my initial app. Django is really stressing my life and it is the most annoying thing i have ever experienced')
