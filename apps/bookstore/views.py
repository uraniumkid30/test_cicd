#  takes a request made by the client(browser) from urls and sends back a nice looking response
# HttpResonse ( a way of communication)

# views can be written in two ways, functions or classes with methods
# using functions
from typing import Any, Dict
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from apps.bookstore.models import Author, Book
from apps.bookstore.forms import BookSearchForm, AddBookForm
from django.views.generic import TemplateView
from django.views.generic.edit import FormView  # generic view
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

# display something random to the user (browser)


def list_authors(request):
    # response
    # print(request.method)
    print(request.GET)  # .get
    # request.POST this used if you have a form in your html and you submit that form
    # request.FILES used whenever someone uploads a file
    # reqest.COOKIES, request.session, request.user
    name_of_author = request.GET.get("name")

    list_of_authors = Author.objects.filter(name__icontains=name_of_author)
    text: str = "<h1>My List Of Authors.</h1>"  # h1 header, h2,h3,h4
    for item in list_of_authors:
        text += f"<p>{item.name}</p>"  # p paragraph element
    return render(
        request, "author.html"
    )  # creates an html file for you on your behalf ,
    # then displays an informtion you set in that html file

    # render(request, "path to your html", data)


def list_books(request):
    return HttpResponse("hey my list of books")


class AuthorView(View):
    def get(self, request):
        print(request.GET)  # .get
        # request.POST this used if you have a form in your html and you submit that form
        # request.FILES used whenever someone uploads a file
        # reqest.COOKIES, request.session, request.user
        name_of_author = request.GET.get("name")

        list_of_authors = Author.objects.all()  # filter(name__icontains=name_of_author)
        my_data = {
            "test_author": "Jeffery",
            "authors": [
                "Dan Brown",
                "William Shakespare",
                "George Owell",
                "Jeffery ",
            ],
            "authors_from_db": list_of_authors,
        }
        # return HttpResponse(text)
        return render(request, "author.html", my_data)

    # def post():
    #     pass


# jinja templating

# we create a view connected to our form
# we want to render our form
# RemplateView is a simple Django view used to render a template with the context data

# class Browse(TemplateView):
#     template_name = "search.html"
#     def get_context_data(self, *args, **kwargs):
#         return {"my_form": SearchForm()}

# the user visits the page
# Django calls the get_context_data()
# it returns a dictionary containing the form
# the form will be passed to the search.html and allow
# the user to interact with

# TemplateView only requires the template name and optionally the contt data
# FormView requires a form class, a success URL, and a method to handle sumbmission

# we can do the same by using the FormView

# class Browse(FormView):
#     template_name = "search.html"
#     form_class = SearchForm

#     success_url = reverse_lazy('success') #specific urls to load ater submission

#     def form_valid(self, form):
#         #Perform actions with the valid form data
#         #for example send a confirmation email, save the data to database
#         return super().form_valid(form)
# I am calling the form from the FormView in forms.py
# Inside the form_valid we will have our custom logic

# really good when we have not only to display data but also submit data


# class SuccessView(TemplateView):
#     template_name = 'success.html'

# connection between view-form-template
# class Browse(FormView):
#     template_name = "book_search.html" #the template where the form is passed and rendered
#     #which form to use???
#     form_class = BookSearchForm

#     def get_context_data(self, **kwargs): #---> data sent to the template
#         context = super().get_context_data(**kwargs)

#         #we create an instance of the BookSearchForm with data from GET request
#         #initialize the form with GET data
#         form = self.form_class(self.request.GET)
#         #without this line the form will be reset after every search
#         #automatically you are saying the form still need to process and validate the incoming get request

#         if form.is_valid():
#             #if it is valid we get cleaned data from the form
#             search_a_book = form.cleaned_data.get("search_a_book", "")
#             category= form.cleaned_data.get("category", "")

#             #.cleaned_data.get("field_name", default_value): gets the validated input from the form fields
#             #search_a_book that stores the book title that the user searched for
#             #stores category that user selected

#             #start with all the books that we have in the database
#             books = Book.objects.all()
#             #if there is a query (the user searched for a book title)
#             if search_a_book:
#                 books = books.filter(title__icontains=search_a_book) #filter title
#             if category:
#                 books = books.filter(category=category) #category field model = category field form (input user)
#             #add the filtered books to the context dictionary to be rendered in the template
#             #this context is to pass the data to the template
#             context["books"] = books
#         #add the form instance (valid or invalid) to the context, so it can be rendered in the template
#         context["form"] = form #ensure that the validated form is in the context and it will be passed in the template
#         return context #return the context data to be passed in the template

# Sends the context (books + form ) to the template (book_search.html)
# book_search.html will have:
# {{ form }} --> the form users interact with
# {% for book in books %} ---> the filtered books to be displayed

# In django views can be implemented in two primary ways:
# -FBVs functions
# -CBVs classes


# built in decorator
@login_required(login_url="/login/")  # Redirect to login if not authenticated
def add_book(request):
    print("🔹 Received request:", request.method)

    if request.method == "POST":
        form = AddBookForm(
            request.POST, request.FILES
        )  #  Include request.FILES for file upload
        print("📥 Form data received:", request.POST)
        print("📂 File data received:", request.FILES)

        if form.is_valid():
            print("✅ Form is valid!")

            # Check if title contains the word "banned", example of more logic
            title = form.cleaned_data.get("title", "").lower()
            if "banned" in title:
                form.add_error("title", "This title contains a restricted word.")
                print("🚫 Error: Title contains a restricted word.")
            else:
                print("💾 Saving book to the database...")
                form.save()  # ✅ Save the book to the database
                print("🔄 Redirecting to success page...")
                return redirect("success")  # ✅ Redirect to success page

        # If form is invalid, show errors
        print("❌ Form errors:", form.errors)

    else:
        print("📝 GET request, showing empty form.")
        form = AddBookForm()  # ✅ Empty form for GET request

    print("🎨 Rendering add_book.html with form.")
    return render(
        request, "add_book.html", {"form": form}
    )  # ✅ Ensure valid response always


# HttpResponse object. It returned None instead
# it comes because the if the nethod is different from POST we will return anything
# it will give to us a NoneOvjet type and so erro
# view
# template
# url


def success_view(request):
    return render(request, "success.html")  # a simple success page


class Browse(FormView):
    template_name = (
        "book_search.html"  # the template where the form is passed and rendered
    )
    # which form to use???
    form_class = BookSearchForm

    def get_context_data(self, **kwargs):  # ---> data sent to the template
        context = super().get_context_data(**kwargs)

        # we create an instance of the BookSearchForm with data from GET request
        # initialize the form with GET data
        form = self.form_class(self.request.GET)
        # without this line the form will be reset after every search
        # automatically you are saying the form still need to process and validate the incoming get request

        if form.is_valid():
            # if it is valid we get cleaned data from the form
            search_a_book = form.cleaned_data.get("search_a_book", "")
            category = form.cleaned_data.get("category", "")

            # .cleaned_data.get("field_name", default_value): gets the validated input from the form fields
            # search_a_book that stores the book title that the user searched for
            # stores category that user selected

            # check the books that are approved in the database
            books = Book.objects.filter(approved=True)  # only fecth approved books

            # start with all the books that we have in the database
            # books = Book.objects.all()
            # if there is a query (the user searched for a book title)
            if search_a_book:
                books = books.filter(title__icontains=search_a_book)  # filter title
            if category:
                books = books.filter(
                    category=category
                )  # category field model = category field form (input user)
            # add the filtered books to the context dictionary to be rendered in the template
            # this context is to pass the data to the template
            context["books"] = books
        # add the form instance (valid or invalid) to the context, so it can be rendered in the template
        context["form"] = (
            form  # ensure that the validated form is in the context and it will be passed in the template
        )
        return context  # return the context data to be passed in the template
