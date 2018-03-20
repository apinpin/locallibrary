from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre

# Create your views here.

def index(request):
    """
    View function for home page of site. 
    """
    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact = 'a').count()
    num_authors = Author.objects.count() # The 'all()' is implied by default.
    num_genres = Genre.objects.all().count()
    num_books_startswith_a = Book.objects.filter(title__startswith='A').count()

    # Render the HTML template index.html with the data in the context variable.
    return render(
        request,
        'index.html',
        context={'num_books':num_books, 'num_instances':num_instances, 'num_instances_available':num_instances_available, 'num_authors':num_authors, 'num_genres':num_authors, 'num_books_startswith_a':num_books_startswith_a}
    )

    