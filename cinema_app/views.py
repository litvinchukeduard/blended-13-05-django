from django.shortcuts import render, redirect

from .models import Movie, Cinema
from .forms import MovieForm, CinemaForm

def main(request):
    return render(request, 'cinema_app/index.html')

def movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = Movie()
            movie.title = form.cleaned_data['title']
            movie.director = form.cleaned_data['director']
            movie.duration = form.cleaned_data['duration']
            movie.save()
            return redirect('main page')
    else:
        movies = Movie.objects.all()
        # for movie in movies:
        form = MovieForm()
        return render(request, 'cinema_app/movies.html', {'movies': movies, 'form': form})

def cinema(request):
    if request.method == 'POST':
        form = CinemaForm(request.POST)
        if form.is_valid():
            print('is valid')
            cinema = Cinema()
            cinema.name = form.cleaned_data['name']
            cinema.location = form.cleaned_data['location']
            cinema.capacity = form.cleaned_data['capacity']
            cinema.save()
            return redirect('main page')
    else:
        cinema = Cinema.objects.all()
        # for movie in movies:
        form = CinemaForm()
        return render(request, 'cinema_app/cinema.html', {'cinema': cinema, 'form': form})