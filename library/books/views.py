from django.views.generic import ListView

from .models import Book

class BookListView(ListView):
    """ renders a list of all books."""
    model = Book
    template_name = 'book_list.html'

# Create your views here.
