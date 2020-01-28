from .models import Book


def total_books(request):
    all_bools =  Book.objects.all()
    counter = all_books.count()
    return{'counter':counter}