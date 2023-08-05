from django.urls import path 
from watchlist_app.api.views import movie_list ,movie_details

urlpatterns = [
    path('list/',movie_list, name='movie-list'),
    path("<str:pk>/",movie_details,name="movie-details")
  
]
