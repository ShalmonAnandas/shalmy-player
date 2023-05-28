from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name="home"),
    path("tv_shows", views.tv_shows, name="tv_shows"),
    path("movies", views.movies, name="movies"),
    path("search", views.search_results, name="search"),
    path("tv_episode_select", views.tv_episode_select, name="tv_episode_select"),
]
