from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
import random
from .forms import BookForm
from .models import Book


def home(request):
    return HttpResponse("This is the homepage")


def welcome(request):
    slogans = [
        "Libraries make shhh happen.",
        "Believe in your shelf.",
        "Need a good read? We’ve got you covered.",
        "Check us out. And maybe one of our books too.",
        "Get a better read on the world."
    ]

    slogan = random.choice(slogans)
    return render(request, 'welcome.html', {'slogan': slogan})


def list_books(request):
    context = {'books': Book.objects.all()}
    return render(request, 'books.html', context)


def get_book(request, book_id):
    return HttpResponse(f"You're requesting book with book_id: {book_id}")


def get_book(request, book_id):
    foo = request.GET.get('foo', 0)
    bar = request.GET.get('bar', 0)
    return HttpResponse(f"You're requesting book with book_id: {book_id}, foo: {foo}, bar: {bar}")


def create_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            try:
                form.save()
            except:
                form.add_error(None, "It was not possible to save this book to the database.")
            else:
                path = reverse('list_books')
                return HttpResponseRedirect(path)
    else:
        form = BookForm()
    return render(request, 'create_book.html', {'form': form, 'button_text': 'Create'})


def update_book(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        raise Http404(f"Could not find book with primary key {book_id}")

    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            try:
                form.save()
            except:
                form.add_error(None, "It was not possible to save this book to the database.  Check the ISBN number.")
            else:
                path = reverse('list_books')
                return HttpResponseRedirect(path)
    else:
        form = BookForm(instance=book)
    return render(request, 'update_book.html', {'book_id': book_id, 'form': form, 'button_text': 'Update'})
