from django.shortcuts import render
from django.http import HttpResponse
from  .models import Category, Page
from django.views.generic.list import ListView


def index(request):
    # Querying the database for for a list of all categories
    # Ordering the category list in descending order
    # Retrieving only to 5 categories
    category_list = Category.objects.order_by('-likes')[:5]

    # A dictionary to pass to the template engine
    context = {'categories': category_list}

    # Rendering a response to the client
    return render( request,'rango/index.html', context)


# class CategoryListView(ListView):
#     model = Category
#     template_name = 'rango/index.html'
#     ordering = ['-likes']

def about(request):
    # A dictionary to pass to the template engine
    context = {'boldmessage': 'I am a bold font of the context on the About Page '}
    # Rendering a response to the client
    return render(request, 'rango/about.html', context)


def category(request, category_name_url):
    category_name = category_name_url.replace('_', ' ')
    print(category_name_url)
    print(category_name)

    context = {'category_name': category_name}

    try:
        category = Category.objects.get(name=category_name)


        pages = Page.objects.filter(category=category)

        context['pages'] = pages
        context['category'] = category

    except Category.DoesNotExist:
        pass

    return render(request, 'rango/category.html', context)
