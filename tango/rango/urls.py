from django.urls import path
from . import views

urlpatterns = [
    path('rango/', views.index, name='index'),
    path('rango/about/', views.about, name='about')
]