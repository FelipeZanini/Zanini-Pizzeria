from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import EmailInput, TextInput
from django.contrib.auth.models import User



class RegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email', 'password1', 'password2']
        widgets = {
            'username': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Username'
                }),
            'first_name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'First Name'
                }),
            'email': EmailInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Email'
                }),
        }


class LoginForm(forms.Form):
    username = forms.CharField(max_length=65, widget=forms.TextInput(
        attrs={'placeholder': 'Username',
               'style': 'width: 300px;',
               'class': 'form-control'}))
    password = forms.CharField(max_length=65, widget=forms.PasswordInput(
        attrs={'placeholder': 'Password',
               'style': 'width: 300px;',
               'class': 'form-control'}))