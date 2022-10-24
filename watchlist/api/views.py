from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from watchlist.models import Movie
from watchlist.api.serializers import MovieSerializer


@api_view(['GET', 'POST'])
def movie_list(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response({'status': 'success', 'data': serializer.data})

    if request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        else:
            return Response({'status': 'fail', 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def movie_details(request, pk):
    if request.method == 'GET':
        try:
            movie = Movie.objects.get(pk=pk)
            serializer = MovieSerializer(movie)
            return Response({'status': 'success', 'data': serializer.data})
        except Movie.DoesNotExist:
            data = {}
            data['status'] = 'fail'
            data['error'] = 'Movie with requested id was not found!'
            return Response(data, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        try:
            movie = Movie.objects.get(pk=pk)
            serializer = MovieSerializer(movie, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'status': 'success', 'data': serializer.data})
            else:
                return Response(serializer.errors)
        except Movie.DoesNotExist:
            data = {}
            data['status'] = 'fail'
            data['error'] = 'Movie with requested id was not found!'
            return Response(data, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        try:
            movie = Movie.objects.get(pk=pk)
            movie.delete()
            return Response({'status': 'success', 'data': 'Movie successfully deleted!'})
        except Movie.DoesNotExist:
            data = {}
            data['status'] = 'fail'
            data['error'] = 'Movie with requested id was not found!'
            return Response(data, status=status.HTTP_404_NOT_FOUND)
