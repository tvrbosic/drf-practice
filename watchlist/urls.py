from django.urls import path

from .views import MovieListView, MovieDetailsView, StreamPlatformView, StreamPlatformDetailsView

urlpatterns = [
    path('movie/', MovieListView.as_view(), name='movie-list'),
    path('movie/<int:pk>/', MovieDetailsView.as_view(), name='movie-details'),
    path('platform/', StreamPlatformView.as_view(), name='platform-list'),
    path('platform/<int:pk>/', StreamPlatformDetailsView.as_view(),
         name='movie-details'),
]
