from django import forms
from apps.bookstore.models import Book

# What is our goal?
# If a user provides a search query, it filters books based on the title
# If they select a category, it filters books within the category
# If they leave empty, we show all the books (we list all the books available)
# we are going to filter, search so when user submit the data is not mofiyng the data on the server


class BookSearchForm(forms.Form):
    search_a_book = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={"placeholder": "Search books..."}
        ),  # suggestion what user has to do
    )

    # filter for all the categories, I look as user inside every category
    # filer for a specific category, so for example I look for a book in the science category
    category = forms.ChoiceField(
        choices=[("", "All Categories")]
        + list(Book._meta.get_field("category").choices),
        required=False,
        # category needs to be selected
        widget=forms.Select(),
    )


# When user select all categories the form sends '' as value, in the backend
# category == '' so that it knows that user was not selecting a specific category
# this allows the form to return all books

# I need also to get the predifined choices, access the category field in the book Model

# Hey Django, tell me everyhing about the category filed in the Book model!
# _meta stores informations about a model like fields, relationship
# When you defie a model, _meta is automatically attached to it

# >>> category_field=Book._meta.get_field('category')
# >>> print(category_field.choices) I want to get the choices defined for that field
# convert teh choices into a list that can be used in the form
# If the categorsy change in the model, the form will be automatically updated


# I want the user to add a new book in the database for existing authors
# I want that this operation has to be approved from the admin
# and only then the new books will be shown in the list of books in the browse
# ---> now the data we send back are actually creating a modification to the data on the server
# self-study to add also a book with new author, try to make the user update a book but make admin to approve

# CREATE A MODEL FORM
# a Model form automatically generates fields based on the model fields and handles associated validations


class AddBookForm(forms.ModelForm):
    book_file = forms.FileField(required=False, label="Upload Book")
    book_link = forms.URLField(required=False, label="Book URL")

    class Meta:
        model = Book
        fields = [
            "title",
            "author",
            "category",
            "book_file",
            "book_link",
        ]  # you can add more existing fields or even new fields to the form


# you can customize with widget
