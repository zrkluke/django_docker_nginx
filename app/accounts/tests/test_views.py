from django.test import TestCase
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.urls import reverse


class LoginViewTestCase(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create(username="test_user",
                                        password=make_password("test_password"))
    
    def test_login_success(self):
        data = {
            'username': 'test_user',
            'password': 'test_password',
        }
        response = self.client.post(reverse('accounts:login'), data=data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('accounts:index'))