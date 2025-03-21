from django.test import TestCase
from django.test import Client
from apps.user.models import User
from django.urls import reverse

# Create your tests here.

# 1. we want to check if the routing for home page is correct
# 2. we want to check if the home page contains what we want
# 3. we want to see if a user can actually login
# 4. we want to see if a user can log out
# 5. we want to see what happens if we login with the wrong credentials


class UrlTestCase(TestCase):
    def setUp(self):
        # read the json file
        for item in json_file: # {"username": "john_kennedy","password": "jfkennedy","email": "jfken@example.com"}
            User.objects.create(**item)
        self.browser = Client()

    def test_homepage_route(self):
        # self.client.get()# a particular address
        # self.client.post()
        # 127.0.0.1:8000/home/
        url: str = "/home/"
        text = b"Welcome new user!Your session will expire in 60 seconds."
        response = self.browser.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(text in response.content)
        self.assertContains(response, "Welcome new user!Your session")

    def test_user_login(self):
        my_user = User.objects.create(username="my_user")
        my_user.set_password("12345678")
        my_user.save()
        is_user_loggedin = self.browser.login(username="my_user", password="12345678")
        self.assertTrue(is_user_loggedin)

    def test_user_cant_login(self):
        my_user = User.objects.create(username="my_user")
        my_user.set_password("123456")  # the user forgets their password
        my_user.save()
        is_user_loggedin = self.browser.login(username="my_user", password="12345678")
        self.assertFalse(is_user_loggedin)

    def test_user_logout(self):
        response = self.browser.get(reverse("logout_user"))
        self.assertRedirects(response, reverse("login"))
