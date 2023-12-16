from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from books.models import Book

class APITests(APITestCase):
    """ Test the API"""
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title='Harry Potter',
            subtitle='The Chamber of Secrets',
            author='J. K. Rowling',
            isbn='9780439064873',
        )
    
    def test_api_listview(self):
        """ Test the api list view"""
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.count(), 1)
        self.assertContains(response, self.book)



# Create your tests here.
