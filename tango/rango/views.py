from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    # A dictionary to pass to the template engine
    context = {'boldmessage':'I am a bold font of the context  '}
    # Rendering a response to the client
    return render( request,'rango/index.html', context)


def about(request):
    # A dictionary to pass to the template engine
    context = {'boldmessage': 'I am a bold font of the context on the About Page '}
    # Rendering a response to the client
    return render(request, 'rango/about.html', context)


