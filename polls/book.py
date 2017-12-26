from django.http import HttpResponse
from django.views.generic import ListView
from polls.models import Book
from var_dump import var_dump

class BookListView(ListView):

    model = Book
    def head(self, *args, **kwargs):
        last_book = self.get_queryset().latest('publication_date')
        response = HttpResponse('')
        # RFC 1123 date format
        response['LastModified'] = last_book.publication_date.strftime('%a, %d %b %Y %H:%M:%S GMT')

        return response