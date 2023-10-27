from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm, 
    UsernameField,
)
from django.utils.translation import gettext_lazy as _


User = get_user_model()


class CustomRegisterForm(UserCreationForm):
    username = forms.CharField(
        label="帳號",
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control border border-dark',
            'placeholder': '設定您的帳號' }
            ),
    )

    password1 = forms.CharField(
        label="設定密碼",
        required=True,
        max_length=18,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control border border-dark',
            'type': 'password',
            'autocomplete': 'new-password',
            'placeholder': '8-18個英數字元，請區分大小寫', }
            ),
    )

    password2 = forms.CharField(
        label="確認密碼",
        required=True,
        max_length=18,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control border border-dark',
            'type': 'password',
            'autocomplete': 'new-password',
            'placeholder': '再次輸入您的密碼', }
            ),
    )

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""


class UserLoginForm(AuthenticationForm):

    username = UsernameField(
        label="帳號",
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control border border-dark',
            'placeholder': '請輸入帳號', }
            ),
        error_messages={
            'invalid': '帳號錯誤，請重新輸入' },
        )
    
    password = forms.CharField(
        label="密碼",
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control border border-dark',
            'placeholder': '請輸入密碼',
            'type': 'password', }
            ),
        error_messages={
            'invalid': '密碼錯誤' },
        )

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.label_suffix = ""

    def login(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user
