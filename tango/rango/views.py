from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    # A dictionary to pass to the template engine
    context = {'boldmessage':'I am a bold font of the context  '}
    # Rendering a response to the client
    return render( request,'rango/index.html', context)


def about(request):
    return HttpResponse("Rango says: Hereis the about page <a href='/rango/' >Index</a?")


