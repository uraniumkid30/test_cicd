"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from apps.resources.views import (
    home as resources_home,
    user_login,
    user_logout,
)

urlpatterns = [
    # admin interface where you can manage data in your application
    path("admin/", admin.site.urls),
    path("home/", resources_home, name="home"),
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout_user"),
    path("materials/", include("apps.bookstore.urls")),
]
