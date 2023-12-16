from django.test import TestCase
from django.urls import reverse

from .models import Book

class BookTests(TestCase):
    """ Test the Book model"""
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title='Harry Potter',
            subtitle='The Chamber of Secrets',
            author='J. K. Rowling',
            isbn='9780439064873',
        )

    def test_book_content(self):
        """ Test the Book model fields"""
        self.assertEqual(f'{self.book.title}', 'Harry Potter')
        self.assertEqual(f'{self.book.subtitle}', 'The Chamber of Secrets')
        self.assertEqual(f'{self.book.author}', 'J. K. Rowling')
        self.assertEqual(f'{self.book.isbn}', '9780439064873')

    def test_book_listview(self):
        """Test the Book list view"""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Harry Potter')
        self.assertTemplateUsed(response, 'books/book_list.html')

# Create your tests here.
