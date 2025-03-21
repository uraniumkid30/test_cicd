from django.shortcuts import render, redirect
from django.http import HttpResponse
import logging
from datetime import date

# built-in form given by Django for the authentication
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.


# views are functions
# def home(request):  # sent by a client (browser)---> URL
#     """This is the home page for my resources"""
#     return HttpResponse(
#         "Welcome to the resources page!"
#     )  # ends a plain text response to the client


# --> the response sent back by Django view


# def home(request):
#     message = "Welcome again"
#     if request.session.get("is_first_visit", True):
#         message = "Welcome new user!"
#         request.session["is_first_visit"] = False
#     return HttpResponse(message)

# the session is is automatically genereted and stored in the cookies

# def home(request):
#     if request.session.get("is_first_visit", True):
#         request.session["is_first_visit"] = False
#     message = json.dumps(request.COOKIES)
#     return HttpResponse(message)


# def home(request):
#     if request.session.get("is_first_visit", True):
#         request.session["is_first_visit"] = False
#     message = request.session.session_key #property of the request session object
#     return HttpResponse(message)

logger = logging.getLogger("my_first_logger")


def send_email():
    if 6 % 2 == 0:
        # info type of log
        #print("Email sent to my friend")
        logger.error("Email Sent to my Friend.")
    else:
        # error type of log
        print("Email not sent")
    # critical type of log is
    # while 100 > 10:
    #     # critical type of log
    #     print(100 - 10)


def home(request):
    message = ""

    # check if user is visiting for the first time
    if request.session.get("is_first_visit", True):
        message = "Welcome new user!"
        request.session["is_first_visit"] = False

        today = date.today()

        # check if today is Wed.
        if today.weekday() == 2:
            message += "Today is Wed!"

        # set session expiration to 60 seconds
        request.session.set_expiry(60)
        message += "Your session will expire in 60 seconds."
    print(message)
    send_email()

    return HttpResponse(message)


# authentication user
# -function base (we do together)
# -class base (as self-study) is more appropriate


def user_login(request):
    if request.method == "POST":
        # we are using a built-in authentication form
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():

            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            # authenticate the user
            # we need to check the username and password against the
            # database using the authentication system (auth_user table)
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)  # ---> to log the user in
                return redirect("home")  # redirect to the home page
            else:
                # Invalid login credentials
                return redirect(
                    "login"
                )  # we need to get back to the login, name=login in the url

    else:
        form = AuthenticationForm()

        # give the response
    return render(request, "login.html", {"form": form})


# from the login you go to the homepage the session id is generated
# after 60 seconds it gots expired so all the data that are stored
# they will be gone and new sessionid will be generated
# you will need to login again because the session is expired


def user_logout(request):
    logout(request)
    # this will end the session, flush means close and cancel the session data
    return redirect("login")


def create_user(request):
    plain_password = "12345678"
    hashed_password = make_password(plain_password)
    check_password(plain_password, hashed_password)

    # in your example
    # user.password is hashed
    check_password("123456", user.password)
