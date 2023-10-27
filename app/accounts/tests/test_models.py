from django.test import TestCase
from accounts.models import CustomUser


class CustomUserTestCase(TestCase):
    def setUp(self):
        CustomUser.objects.create(username="test_user", password="test_password")

    def test_custom_user_str(self):
        user = CustomUser.objects.get(username="test_user")
        self.assertEqual(str(user), user.username)
