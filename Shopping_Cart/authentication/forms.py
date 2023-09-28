from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


CLASS_CSS = 'font-control'


class SigninForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'your username',
        'class': CLASS_CSS
    }))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        'placeholder': 'your password',
        'class': CLASS_CSS
    }))

    class Meta:
        model = User
        fields = ('username', 'password')


class SignupFrom(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'your username',
        'class': CLASS_CSS
    }))

    name = forms.CharField(label='Full Name', widget=forms.TextInput(attrs={
        'placeholder': 'your name',
        'class': CLASS_CSS
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'your valid email',
        'class': CLASS_CSS
    }))

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        'placeholder': 'your password',
        'class': CLASS_CSS
    }))
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput(attrs={
        'placeholder': 'repeat password',
        'class': CLASS_CSS
    }))

    class Meta:
        model = User
        fields = ('username', 'name', 'email', 'password1', 'password2')