from django.shortcuts import render, HttpResponse
import tmdbsimple as tmdb
from itertools import zip_longest
import requests
import json

tmdb.API_KEY = "87d5585a5497b373679e8bdc7d6f0d22"


def index(request):
    return render(request, "index.html")


def search_func(search_term):
    search_term = search_term.split(" ")
    search_term = "%20".join(search_term)
    url = f"https://api.themoviedb.org/3/search/multi?query={search_term}&include_adult=false&language=en-US&page=1"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4N2Q1NTg1YTU0OTdiMzczNjc5ZThiZGM3ZDZmMGQyMiIsInN1YiI6IjYyMWRlNjY2ZDM4YjU4MDAxYmY0NDM3NSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.JQAtkdBkGc2UNLbGZltTqowTCKCRyoGFL1OkwuWTZz8",
    }

    response = requests.get(url, headers=headers)
    json_data = json.loads(response.text)
    results = json_data["results"]

    movie_title_list = []
    movie_description_list = []
    movie_poster_list = []
    movie_id_list = []

    tv_title_list = []
    tv_description_list = []
    tv_poster_list = []
    tv_id_list = []

    for result in results:
        if result.get("media_type") == "movie" and result.get("vote_count") >= 100:
            movie_title_list.append(result.get("title"))
            movie_description_list.append(result.get("overview"))
            movie_poster_list.append(result.get("poster_path"))
            movie_id_list.append(result.get("id"))

        if result.get("media_type") == "tv":
            tv_title_list.append(result.get("name"))
            tv_description_list.append(result.get("overview"))
            tv_poster_list.append(result.get("poster_path"))
            tv_id_list.append(result.get("id"))

    context = {
        "movie_data": zip_longest(
            movie_title_list,
            movie_description_list,
            movie_poster_list,
            movie_id_list,
        ),
        "tv_data": zip_longest(
            tv_title_list,
            tv_description_list,
            tv_poster_list,
            tv_id_list,
        ),
    }

    return context


def search_results(request):
    search_term = request.GET.get("q")
    context = search_func(search_term)

    return render(request, "search_results.html", context)


def movies(request):
    return render(request, "movies.html")


def tv_shows(request):
    return render(request, "tv_shows.html")


def tv_episode_select(request):
    var = request.GET.get["name"]
    print(var)
    return render(request, "tv_episode_select.html")
