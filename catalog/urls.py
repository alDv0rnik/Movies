from django.contrib import admin
from django.urls import path

from catalog import views


urlpatterns = [
    path('', views.catalog_view, name='movies_list'),
    path('fav/<int:movie_id>', views.favourite_add, name='favourite'),
]
