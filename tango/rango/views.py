from django.shortcuts import render
from django.http import HttpResponse
from  .models import Category, Page


def index(request):
    # Querying the database for for a list of all categories
    # Odering the category list in descending order
    # Retrieving only to 5 categories
    category_list = Category.objects.order_by('-likes')[:5]
    
    context = {'categories': category_list}

    # A dictionary to pass to the template engine
    context = {'boldmessage':'I am a bold font of the context  '}
    # Rendering a response to the client
    return render( request,'rango/index.html', context)


def about(request):
    # A dictionary to pass to the template engine
    context = {'boldmessage': 'I am a bold font of the context on the About Page '}
    # Rendering a response to the client
    return render(request, 'rango/about.html', context)


