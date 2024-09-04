from django.shortcuts import render
from .models import Book
from author.models import Author
from .serializers import BookSerializer, BookListSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from .permissions import IsAuthorOrAdmin


class BookListView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookListSerializer


class BookCreateView(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        if user.is_staff:
            author_name = self.request.data.get('author_name')
            if author_name:
                author, created = Author.objects.get_or_create(name=author_name)
                serializer.save(author=author)
            else:
                raise ValueError("Admin users must provide 'author_name'.")
        else:
            serializer.save()

    def create(self, request, *args, **kwargs):
        if request.user.is_staff:
            if 'author_name' not in request.data:
                return Response({"author_name": "required for admins"}, status=status.HTTP_400_BAD_REQUEST)
        return super().create(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        if request.user.is_staff:
            if 'author_name' not in request.data:
                return Response({"author_name": "required for admins"}, status=status.HTTP_400_BAD_REQUEST)
        return super().create(request, *args, **kwargs)


class BookDetailUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'pk'
    permission_classes = [IsAuthorOrAdmin, ]

