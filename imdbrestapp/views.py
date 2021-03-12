from django.shortcuts import render
from .models import Movie
from .serializer import MovieSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

class MovieList(ListAPIView):
       queryset = Movie.objects.all()
       serializer_class = MovieSerializer
       filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
       
       ordering_fields = ['name','rating','release_date', 'duration']
       search_fields = ['name','desc'] 
     
@api_view(['POST'])
def CreateMovie(request):
    serializer = MovieSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def UpdateMovie(request,id):
    movie = Movie.objects.get(id=id)
    serializer = MovieSerializer(instance=movie, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def DeleteMovie(request,id):
    movie = Movie.objects.get(id=id)
    movie.delete()

    return Response("Movie successfully delted")



       
       
       
