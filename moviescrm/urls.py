"""
URL configuration for moviescrm project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from movie_app.views import MoviesCreateView,MoviesListView,TheatreView,TheatreList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',MoviesCreateView.as_view(),name="movies"),
    path('movies_list/',MoviesListView.as_view(),name="movies_list"),
    path('theatre/',TheatreView.as_view(),name="theatre"),
    path('theatre_list/',TheatreList.as_view(),name="theatre_list"),
]
