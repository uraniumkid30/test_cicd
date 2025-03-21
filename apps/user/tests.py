from django.test import TestCase  # everything in unittest is contained here
from apps.user.models import User, Profile

# Create your tests here.
# 1. test if i can create a user from models
# 2. test if i can create a user without complete fields
# 3. test if i can view a users profile after creating a user
# 4. want to see how the profile looks like


class ModelTestCase(TestCase):
    # rule each method has to start with the keyword test
    def test_user_model(self):
        my_user = User.objects.create(
            username="test_user",
            password="123456",
        )  # created user
        self.assertEqual(my_user.username, "test_user")
        self.assertEqual(my_user.password, "123456")

    def test_user_incomplete_fields(self):
        # whats is the interpretation
        # we will need to change the model later
        bad_user = User.objects.create(password="123456")
        self.assertEqual(bad_user.password, "123456")

    def test_user_can_see_profile(self):
        # signals
        my_user = User.objects.create(
            username="test_user",
            password="123456",
        )
        #self.assertIsNotNone(my_user.profile.bio)
        profile_avaible: bool = hasattr(my_user, "profile")
        self.assertFalse(profile_avaible)
