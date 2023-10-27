from django.contrib import admin
from django.urls import path, include

from catalog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('catalog/', include('catalog.urls')),
]

handler404 = views.pageNotFound
