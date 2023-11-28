from django.urls import path
from catalog import views


urlpatterns = [
    path('', views.catalog_view, name='movies_list'),
    path('fav/<int:movie_id>', views.favourite_add, name='favourite'),
    path('favourites', views.favourite_list, name='favourite_list'),
    path('<slug:movie_slug>', views.movie_detail_view, name='movie_details'),
]
