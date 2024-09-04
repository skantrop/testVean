from django.urls import path
from .views import AuthorListView, AuthorDetailUpdateDestroyView, AuthorCreateView


urlpatterns = [
    path('list/', AuthorListView.as_view()),
    path('create/', AuthorCreateView.as_view()),
    path('<int:pk>/', AuthorDetailUpdateDestroyView.as_view()),
]