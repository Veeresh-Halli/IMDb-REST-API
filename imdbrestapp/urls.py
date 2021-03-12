from django.urls import path
from . import views

urlpatterns =[
    path('movielist/',  views.MovieList.as_view(), name='movielist'),
    path('createmovie/',  views.CreateMovie, name='createmovie'),
    path('updatemovie/<int:id>/',  views.UpdateMovie, name='updatemovie'),
    path('deletemovie/<int:id>/',  views.DeleteMovie, name='deletemovie'),
]