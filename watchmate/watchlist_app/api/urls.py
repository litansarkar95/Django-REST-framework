from django.urls import path 
#from watchlist_app.api.views import movie_list ,movie_details
from watchlist_app.api.views import WatchListAV, WatchDetailsAV ,StreamPlatformAV,StreamPlatformDetailsAV

urlpatterns = [
    path('list/',WatchListAV.as_view(), name='movie-list'),
    path("<str:pk>",WatchDetailsAV.as_view(),name="movie-detail"), 
    path("stream/",StreamPlatformAV.as_view(), name='stream'),
    path("stream/<str:pk>",StreamPlatformDetailsAV.as_view(), name='stream-detail'),
  
]


