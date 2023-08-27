from django.urls import path 
#from watchlist_app.api.views import movie_list ,movie_details
from watchlist_app.api.views import MovieListAV, MovieDetailsAV

urlpatterns = [
    path('list/',MovieListAV.as_view(), name='movie-list'),
    path("<str:pk>/",MovieDetailsAV.as_view(),name="movie-details"), 
  
]


