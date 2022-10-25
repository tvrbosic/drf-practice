from django.urls import path

from .views import MovieListView, MovieDetailsView

urlpatterns = [
    path('list/', MovieListView.as_view(), name='movie-list'),
    path('<int:pk>/', MovieDetailsView.as_view(), name='movie-details'),
]
