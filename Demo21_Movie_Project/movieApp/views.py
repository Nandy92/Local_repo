from django.shortcuts import render
from movieApp.models import Movie
# Create your views here.
from . import forms

def index_view(request):
    return render(request,'movieApp/index.html')

def add_movie_view(request):
    form=forms.MovieForm()
    if request.method=='POST':
        form=forms.MovieForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
        return index_view(request)
    return render(request,'movieApp/addmovie.html',{'form':form})

def list_movie_view(request):
    movies_list=Movie.objects.all().order_by('-rating')
    return render(request,'movieApp/listmovie.html',{'movies_list':movies_list})
