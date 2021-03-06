import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango.settings')

import django
django.setup()

from rango.models import  Page, Category


def populate():
    python_cat = add_cat('Python', views=128, likes=64)

    add_page(cat=python_cat, title="Official Python Tutorial", url="py.org")

    add_page(cat=python_cat, title="Official Python Tutorial New", url="python.org")

    add_page(cat=python_cat, title="Official Python Tutorial By David", url="pythonbasics.org")

    django_cat = add_cat('Django', views=64, likes=32)

    add_page(cat=django_cat, title="Django Basics Tutorial", url="djangobasics.org")

    add_page(cat=django_cat, title="Official Django Tutorial",  url="django.org")

    add_page(cat=django_cat, title="Django 2.oTutorial", url="django2.org")

    frame_cat = add_cat("Other Frameworks", views=32, likes=16)

    add_page(cat=frame_cat, title="flask", url="flask.org")

    add_page(cat=frame_cat, title="bottle", url="bottle.org")

    add_page(cat=frame_cat, title="shark", url="shark.org")

    # print out what we have added to the user
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print("- {0} - {1} ".format(str(c), str(p)))


def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title, url=url, views=views)[0]
    return p


def add_cat(name, views, likes):
    c = Category.objects.get_or_create(name=name, views=views, likes=likes)[0]
    return c


# start execution here
if __name__ == '__main__':
    print("Starting Rango population Script")
    populate()
