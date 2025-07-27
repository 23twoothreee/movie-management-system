from django.urls import path
from .views import MovieView

urlpatterns = [
    path('movies/', MovieView.as_view(), name='movie-create'),
    path('movies/<int:pk>/', MovieView.as_view()),
]