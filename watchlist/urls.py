from django.urls import path

from .views import (MoviesView, MovieDetailsView, ReviewsView,
                    ReviewDetailsView, StreamPlatformsView, StreamPlatformDetailsView)

urlpatterns = [
    path('movies/', MoviesView.as_view(), name='movies'),
    path('movie/<int:pk>/', MovieDetailsView.as_view(), name='movie-details'),

    path('movie/<int:pk>/reviews/', ReviewsView.as_view(),
         name='reviews'),  # <---------

    path('platforms/', StreamPlatformsView.as_view(), name='platforms'),
    path('platform/<int:pk>/', StreamPlatformDetailsView.as_view(),
         name='platform-details'),

    path('review/<int:pk>', ReviewDetailsView.as_view(), name='review-details'),
    # path('reviews/>', ReviewsView.as_view(), name='reviews'),


]
