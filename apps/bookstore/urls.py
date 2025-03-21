# holds all the addresses a client(browser)  can go to and it holds information
# about which view can give it a response

# more than one address mapping

from django.urls import path
from . import views


urlpatterns = [
    # path("authors/", views.list_authors),
    path("authors/", views.AuthorView.as_view(), name="my_authors"),
    path("books/", views.list_books, name="my_books"),
    path("browse/", views.Browse.as_view(), name="book-browse"),
    path("add-book/", views.add_book, name="add_book"),
    path(
        "success/", views.success_view, name="success"
    ),  # name=success we pass to the reverse_lazy
]
