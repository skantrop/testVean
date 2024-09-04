from django.urls import path
from .views import BookListView, BookDetailUpdateDestroyView, BookCreateView


urlpatterns = [
    path('list/', BookListView.as_view()),
    path('create/', BookCreateView.as_view()),
    path('<int:pk>/', BookDetailUpdateDestroyView.as_view()),
]