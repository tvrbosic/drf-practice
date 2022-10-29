from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (MoviesView, MovieDetailsView, ReviewsView,
                    ReviewDetailsView, StreamPlatformVS)

router = DefaultRouter()
router.register(r'platforms', StreamPlatformVS, basename='platform')

urlpatterns = [
    path('movies/', MoviesView.as_view(), name='movies'),
    path('movie/<int:pk>/', MovieDetailsView.as_view(), name='movie-details'),
    path('movie/<int:pk>/reviews/', ReviewsView.as_view(), name='reviews'),
    path('review/<int:pk>', ReviewDetailsView.as_view(), name='review-details'),
    path('', include(router.urls))
    #path('platforms/', StreamPlatformsView.as_view(), name='platforms'),
    #path('platform/<int:pk>/', StreamPlatformDetailsView.as_view(), name='platform-details'),
    # path('reviews/>', ReviewsView.as_view(), name='reviews'),
]
