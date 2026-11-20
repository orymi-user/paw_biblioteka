from django.shortcuts import get_object_or_404, render

from .models import Author, Book


def home(request):
    context = {
        "books_count": Book.objects.count(),
        "authors_count": Author.objects.count(),
    }

    return render(
        request,
        "biblioteka/home.html",
        context,
    )


def book_list(request):
    books = Book.objects.all().order_by(
        "title",
    )

    query = request.GET.get(
        "query",
        "",
    )

    available_filter = request.GET.get(
        "available",
        "",
    )

    if query:
        books = books.filter(
            title__icontains=query,
        )

    if available_filter == "yes":
        books = books.filter(
            available=True,
        )

    elif available_filter == "no":
        books = books.filter(
            available=False,
        )

    context = {
        "books": books,
        "query": query,
        "available_filter": available_filter,
    }

    return render(
        request,
        "biblioteka/book_list.html",
        context,
    )


def author_list(request):
    authors = Author.objects.all()

    context = {
        "authors": authors,
    }

    return render(
        request,
        "biblioteka/author_list.html",
        context,
    )


def contact(request):
    return render(
        request,
        "biblioteka/contact.html",
    )


def about(request):
    return render(
        request,
        "biblioteka/about.html",
    )

def book_detail(request, book_id):
    book = get_object_or_404(
        Book,
        id=book_id,
    )

    context = {
        "book": book,
    }

    return render(
        request,
        "biblioteka/book_detail.html",
        context,
    )

def author_detail(request, author_id):
    author = get_object_or_404(
        Author,
        id=author_id,
    )

    context = {
        "author": author,
    }

    return render(
        request,
        "biblioteka/author_detail.html",
        context,
    )