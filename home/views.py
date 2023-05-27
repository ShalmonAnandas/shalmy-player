from django.shortcuts import render, HttpResponse
import tmdbsimple as tmdb
from itertools import zip_longest
tmdb.API_KEY = '87d5585a5497b373679e8bdc7d6f0d22'


def index(request):
    return render(request, 'index.html')


def search_func(search_term):
    search = tmdb.Search()
    response = search.movie(query=search_term)

    title_list = []
    description_list = []
    poster_list = []
    id_list = []
    for result in search.results:
        title_list.append(result['title'])
        description_list.append(result['overview'])
        poster_list.append(result['poster_path'])
        id_list.append(result['id'])
    context = {
        'data': zip_longest(title_list, description_list, poster_list, id_list)
    }

    return context


def search_results(request):
    search_term = request.GET.get('q')
    context = search_func(search_term)

    return render(request, 'search_results.html', context)


def movies(request):
    return render(request, 'movies.html')


def tv_shows(request):
    return render(request, 'tv_shows.html')
