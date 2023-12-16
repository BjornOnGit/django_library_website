from rest_framework import generics

from books.models import Book
from .serializers import BookSerializer

class BookAPIView(generics.ListAPIView):
    """ This class defines the create behavior of our REST API."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Create your views here.
