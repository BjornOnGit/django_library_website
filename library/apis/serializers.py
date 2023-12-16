from rest_framework import serializers

from books.models import Book

class BookSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Book
        fields = ('title', 'subtitle', 'author', 'isbn')
