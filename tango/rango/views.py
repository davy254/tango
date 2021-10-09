from django.shortcuts import render, redirect
from django.http import HttpResponse
from  .models import Category, Page
from django.contrib import  messages
from .forms import CategoryForm, PageForm, UserForm, UserProfileForm
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


def decode_url(category_name_url):
    category_name = category_name_url.replace('_', ' ')
    return category_name


def category(request, category_name_url):
    category_name = decode_url(category_name_url)
    print(category_name_url)
    print(category_name)

    context = {'category_name': category_name, 'category_name_url':category_name_url}

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



def add_pages(request, category_name_url):
    category_name = decode_url(category_name_url)

    if request.method == 'POST':
        form = PageForm(request.POST)

        if form.is_valid():
            page = form.save(commit=False)

            try:
                cat = Category.objects.get(name=category_name)

                page.category = cat
            except Category.DoesNotExist:
                return render(request, 'rango/add_category.html', {'form':form})

            page.views = 0

            page.save()

            return category(request, category_name_url)
        else:
            print(form.errors)
    else:
        form = PageForm()

    context = {'category_name_url':category_name_url, 'category_name':category_name, 'form':form}
    return render(request, 'rango/add_page.html', context)


def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)

            profile.user = user

            if 'picture' in request.FILES:
                profile.picture =request.FILES['picture']

            profile.save()

            registered = True

            username = user_form.cleaned_data.get('username')
            messages.success(request, f'Account for { username} has been created.Try to login now')
            return redirect('login')

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form =UserForm()
        profile_form = UserProfileForm()

    context ={'user_form':user_form,
              'profile_form':profile_form}

    return render(request, 'rango/register.html', context)


