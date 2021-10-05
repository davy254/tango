from django.shortcuts import render
from django.http import HttpResponse
from  .models import Category, Page
from .forms import CategoryForm
from django.views.generic.list import ListView


def index(request):
    # Querying the database for for a list of all categories
    # Ordering the category list in descending order
    # Retrieving only to 5 categories
    category_list_likes = Category.objects.order_by('-likes')[:5]
    category_list_views = Category.objects.order_by('-views')[:5]

    # A dictionary to pass to the template engine
    context = {'categories_likes': category_list_likes,
               'categories_views':category_list_views}

    for category in category_list_likes:
        category.url = category.name.replace(' ', '_')

    for category in category_list_views:
        category.url = category.name.replace(' ', '_')

    # Rendering a response to the client
    return render( request,'rango/index.html', context)


# class CategoryListView(ListView):
#     model = Category
#     template_name = 'rango/index.html'
#     context_object_name = ('categories_likes', 'categories_views')
#
#     def get_queryset(self):
#         categories_likes = Category.objects.order_by('-likes')[:5]
#         categories_views = Category.objects.order_by('-views')[:5]
#         return categories_likes , categories_views

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


def add_category(request):

    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save()

            return index(request)

        else:
            print(form.errors)

    else:
        form = CategoryForm()

    return render(request, 'rango/add_category.html', {'form':form})

