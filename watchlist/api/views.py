from rest_framework.decorators import api_view
from rest_framework.response import Response
from watchlist.models import Movie
from watchlist.api.serializers import MovieSerializer


@api_view(['GET'])
def movie_list(request):
    movies = Movie.objects.all()
    serialized_data = MovieSerializer(movies, many=True)
    return Response(serialized_data.data)


def movie_details(request, pk):
    movie = Movie.objects.get(pk=pk)
    serialized_data = MovieSerializer(movie)
    return Response(serialized_data.data)
