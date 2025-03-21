from .base import *  # we need to extend our base
import environ

env = environ.Env()
environ.Env.read_env(str(BASE_DIR / '.env'))  # read from the .env file

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1"]

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env.str('DB_NAME'),
        'USER': env.str('DB_USER'),
        'PASSWORD': env.str('DB_PWD'),
        'HOST': env.str('DB_HOST'),
        'PORT': env.str('DB_PORT'),
    }
}

#Use cookies for session storage
# SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies' #.db, cookies
# #The signed_cookies backend ensures that session data is securely signed to prevent tampering
# #session age ith the expiring time
# SESSION_COOKIES_AGE = 60 #default value is 60 seconds
# #Ensure that the session expires when the browse closes
# SESSION_EXPIRE_AT_BROWSER_CLOSE = True
# #by default they will have expired in two weeks without extra settings 
# #encrypt the cookies to add some security
# #This forces cookies to be sent only over HTTPS
# SESSION_COOKIE_SECURE = False #use True in production 

#to properly make it work we have to be sure that the session is properly
#installed, configured