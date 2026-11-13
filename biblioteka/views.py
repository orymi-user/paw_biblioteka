from django.shortcuts import render

def home(request):
    return render(request, "biblioteka/home.html")


def book_list(request):
    books = [
        {
            "title": "Solaris",
            "author": "Stanisław Lem",
            "year": 1961,
            "available": True,
        },
        {
            "title": "Lalka",
            "author": "Bolesław Prus",
            "year": 1890,
            "available": False,
        },
        {
            "title": "Hobbit",
            "author": "J.R.R. Tolkien",
            "year": 1937,
            "available": True,
        },
    ]

    context = {
        "books": books,
    }

    return render(
        request,
        "biblioteka/book_list.html",
        context,
    )
def author_list(request):
    return render(
        request,
        "biblioteka/author_list.html",
    )
def contact(request):
    return render(
        request,
        "biblioteka/contact.html",
    )