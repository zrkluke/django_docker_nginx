from django.test import TestCase
from accounts.forms import CustomRegisterForm


class RegisterTestCase(TestCase):
    def setUp(self):
        self.form = CustomRegisterForm

    def test_password_invalid(self):
        data = {
            'username': 'test_user',
            'password1': 'password',
            'password2': 'password'
        }
        form = self.form(data)
        form.is_valid()
        self.assertTrue('password2' in form.errors.keys())
