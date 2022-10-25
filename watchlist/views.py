# ----------------------------------- CLASS BASED VIEWS -----------------------------------
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Movie, StreamPlatform
from .serializers import MovieSerializer, StreamPlatformSerializer
from watchlist import serializers


def response_payload(successful, data=None, message=None, errors=None):
    payload = {}
    payload['status'] = 'success' if successful else 'fail'
    if data is not None:
        payload['data'] = data
    if message is not None:
        payload['message'] = message
    if errors is not None:
        payload['errors'] = errors
    return payload


class MovieListView(APIView):
    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(response_payload(successful=True, data=serializer.data))

    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(response_payload(successful=True, data=serializer.data))
        else:
            return Response(response_payload(successful=False, errors=serializer.errors), status=status.HTTP_400_BAD_REQUEST)


class MovieDetailsView(APIView):
    def get(self, request, pk):
        try:
            movie = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response(response_payload(successful=False, message='Movie with requested id was not found!'), status=status.HTTP_404_NOT_FOUND)

        serializer = MovieSerializer(movie)
        return Response(response_payload(successful=True, data=serializer.data))

    def put(self, request, pk):
        try:
            movie = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response(response_payload(successful=False, message='Movie with requested id was not found!'), status=status.HTTP_404_NOT_FOUND)

        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(response_payload(successful=True, data=serializer.data))
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        try:
            movie = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response(response_payload(successful=False, message='Movie with requested id was not found!'), status=status.HTTP_404_NOT_FOUND)

        movie.delete()
        return Response(response_payload(successful=True, message='Movie successfully deleted!'))


class StreamPlatformView(APIView):
    def get(self, request):
        platforms = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(platforms, many=True)
        return Response(response_payload(successful=True, data=serializer.data))

    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            return Response(response_payload(successful=True, data=serializer.data))
        else:
            return Response(response_payload(successful=False, errors=serializer.errors), status=status.HTTP_400_BAD_REQUEST)


class StreamPlatformDetailsView(APIView):
    def get(self, request, pk):
        try:
            platform = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response(response_payload(successful=False, message='Platform with requested id was not found!'), status=status.HTTP_404_NOT_FOUND)

        serializer = StreamPlatformSerializer(platform)
        return Response(response_payload(successful=True, data=serializer.data))

    def put(self, request, pk):
        try:
            platform = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response(response_payload(successful=False, message='Platform with requested id was not found!'), status=status.HTTP_404_NOT_FOUND)

        serializer = StreamPlatformSerializer(platform, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(response_payload(successful=True, data=serializer.data))
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        try:
            platform = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response(response_payload(successful=False, message='Platform with requested id was not found!'), status=status.HTTP_404_NOT_FOUND)

        platform.delete()
        return Response(response_payload(successful=True, message='Platform successfully deleted!'))


"""
# ----------------------------------- FUNCTION BASED VIEWS -----------------------------------
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from watchlist.models import Movie
from watchlist.api.serializers import MovieSerializer




def response_payload(successful, data=None, message=None, errors=None):
    payload = {}
    payload['status'] = 'success' if successful else 'fail'
    if data is not None:
        payload['data'] = data
    if message is not None:
        payload['message'] = message
    if errors is not None:
        payload['errors'] = errors
    return payload


@api_view(['GET', 'POST'])
def movie_list(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(response_payload(successful=True, data=serializer.data))

    if request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(response_payload(successful=True, data=serializer.data))
        else:
            return Response(response_payload(successful=False, errors=serializer.errors), status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def movie_details(request, pk):
    if request.method == 'GET':
        try:
            movie = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response(response_payload(successful=False, message='Movie with requested id was not found!'), status=status.HTTP_404_NOT_FOUND)

        serializer = MovieSerializer(movie)
        return Response(response_payload(successful=True, data=serializer.data))

    if request.method == 'PUT':
        try:
            movie = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response(response_payload(successful=False, message='Movie with requested id was not found!'), status=status.HTTP_404_NOT_FOUND)

        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(response_payload(successful=True, data=serializer.data))
        else:
            return Response(serializer.errors)

    if request.method == 'DELETE':
        try:
            movie = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response(response_payload(successful=False, message='Movie with requested id was not found!'), status=status.HTTP_404_NOT_FOUND)

        movie.delete()
        return Response(response_payload(successful=True, message='Movie successfully deleted!'))
"""
