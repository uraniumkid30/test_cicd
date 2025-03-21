#apps/bookstore/middlewares/auth_check_middleware.py
from django.urls import resolve, reverse
from django.http import HttpResponseRedirect

class AuthCheckMiddleware:
    #initialize the middleware
    def __init__(self, get_response): #a callable that process the request and returns response
        self.get_response = get_response

    #allow an instance of this calss to be callable as a function 
    #how to process the request and trigger the middleware
    def __call__(self, request):
        print("Middleware is being triggered.") #check if the middleware is triggered.
        
        #check if the user is logged in 
        print(f"User is authenticated: {request.user.is_authenticated}") #True or False

        #get the view name for the current request, resolve has to match the url that we pass
        view_name = resolve(request.path_info).view_name
        print(f"Resolved view name: {view_name}")

        #check if the user is accessing the browse view 
        if view_name == 'book-browse': #the correct name space for the view name (urls.py)
            if not request.user.is_authenticated:
                login_url = reverse('login') #we pass the name for the login view
                print(f"Redirecting to {login_url}")
                return HttpResponseRedirect(login_url)
            
        #if the user is authenticated, proceed with the request
        response = self.get_response(request) #---> go to the Browse view as usual 
        return response


#other features like permission, logging, custom error handling,
#feature flags. 
#The beauty of Django middleware is its ability to intecept requests and responses globally
#so that you can apply various logic to all incoming requests. 

#Exercise:
#make it work for all the requests
